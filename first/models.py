from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150)


    def __str__(self):
        return self.title
        