from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlogForm
from .models import Blogpost

def home(request):
    blogs = Blogpost.objects.all()
    return render(request, 'website/index.html', {'blogs': blogs})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def make_post(request):
    if request.method == "POST":
        form = CreateBlogForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = CreateBlogForm()
    return render(request, 'website/make-post.html',{'form': form})

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

def delete_post(request, blog_id):
    blog = get_object_or_404(Blogpost, pk=blog_id)
    blog.delete()
    return redirect('home')

def post(request, blog_id):
    post = get_object_or_404(Blogpost, pk=blog_id)
    return render(request, 'website/post.html', {'post': post})