from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)

class Article(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete= models.CASCADE)
    # using foreignkey as we have to use reporter on this article class
    headline = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.headline
        