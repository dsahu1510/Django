from django.db import models

# Create your models here.

class Todo(models.Model):
    s_no = models.IntegerField(default=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()

class Meta():
    fields = '__all__'

    def __str__(self):
        return self.title