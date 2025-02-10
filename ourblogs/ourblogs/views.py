from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateBlogForm, CreateUserForm, LoginForm, CommentForm
from .models import Blogpost, Comment

def home(request):
    blogs = Blogpost.objects.all()
    return render(request, 'website/index.html', {'blogs': blogs})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

@login_required(login_url='login')
def make_post(request):
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = CreateBlogForm()
    return render(request, 'website/make-post.html',{'form': form})

@login_required(login_url='login')
def edit_post(request, post_id):
    post = get_object_or_404(Blogpost, pk=post_id)
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateBlogForm(instance=post)
    return render(request, 'website/make-post.html', {'form':form,'post': post,'is_edit': True})

@login_required(login_url='login')
def delete_post(request, blog_id):
    blog = get_object_or_404(Blogpost, pk=blog_id)
    blog.delete()
    return redirect('home')

def post(request, blog_id):
    post = get_object_or_404(Blogpost, pk=blog_id)
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = post
            comment.save()
            return redirect('post', blog_id=post.id)

    return render(request, 'website/post.html', {'post': post, 'form': form, 'comments':comments})

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'website/register.html', {'form': form})



def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Username or Paaaword is incorrect.")
    else:
        form = LoginForm()
    return render(request, 'website/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')