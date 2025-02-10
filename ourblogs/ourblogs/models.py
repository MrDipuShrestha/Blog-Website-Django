from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default="")
    author = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')

    comment = models.TextField(default="")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} on {self.blog.title}"