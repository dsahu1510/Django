from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=10)
    ename = models.CharField(max_length=20) 
    email = models.EmailField()
    econtact = models.CharField(max_length=50)

    def __str__(self):
        return self.ename