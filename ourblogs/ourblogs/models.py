from django.db import models
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
    