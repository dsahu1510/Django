from django.db import models

# Create your models here.

class User(models.Model):
    
    username = models.CharField(max_length=20)
    designation = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class Company(models.Model):
    joining_date = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    user = models.ForeignKey("User", on_delete=models.PROTECT, null=False)


    class Meta:
      verbose_name_plural = "companies"

    def __str__(self):
        return self.location


