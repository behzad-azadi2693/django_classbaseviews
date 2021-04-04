from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150)


    def __str__(self):
        return self.title
        
class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='tcomments')
    name = models.ForrignKey(User, on_delete=models.CASCADE, related_name='author')
    body = models.TextField()

    def __str__(self):
        return self.name
