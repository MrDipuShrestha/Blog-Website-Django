from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blogpost


### Regualr form
# class CreateBlogForm(forms.Form):
#     title = forms.CharField(label='Blog Post Title', widget=forms.TextInput(attrs={"class": "form-control"}))
#     subtitle = forms.CharField(label='Subtitle', widget=forms.TextInput(attrs={"class": "form-control"}))
#     author = forms.CharField(label='Author Name', widget=forms.TextInput(attrs={"class": "form-control"}))
#     image_url = forms.CharField(label='Image URL', widget=forms.TextInput(attrs={"class": "form-control"}))
#     body = forms.CharField(label='Body', widget=forms.TextInput(attrs={"class": "form-control"}))


### modelForm
class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'subtitle', 'body', 'author', 'img_url']  # Model fields to include in the form
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'subtitle': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'author': forms.TextInput(attrs={"class": "form-control"}),
            'img_url': forms.TextInput(attrs={"class": "form-control"}),
        }

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"})) 
