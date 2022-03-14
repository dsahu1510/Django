from django.db import models
from django import forms
# Create your models here.
class main_form(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title