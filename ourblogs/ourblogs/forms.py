from django import forms
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