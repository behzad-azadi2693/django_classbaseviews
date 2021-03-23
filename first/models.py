from django.db import models

# Create your models here.


class Todo(models.models):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        