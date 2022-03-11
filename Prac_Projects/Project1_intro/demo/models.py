from turtle import title
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    Description = models.TextField()
    last_modified = models.DateTimeField(default='')

    def __str__(self):
        return self.title