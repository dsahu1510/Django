from django.db import models

# Create your models here.
class newBooks(models.Model):
    Book_title = models.CharField(max_length=200)
    Book_desc = models.TextField()

    def __str__(self):
        return self.Book_title