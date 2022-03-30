from django.db import models

####################################### many to many relationship in Django ##############################
# Create your models here.
# class Publication(models.Model):
#     title = models.CharField(max_length=30)


#     def __str__(self):
#         return self.title

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     publications = models.ManyToManyField(Publication)


#     def __str__(self):
#         return self.headline

####################################### One to One relationship in Django ##############################

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place"%self.name
    
class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant"%self.place.name


class Waiter(models.Model):
    restaraunt = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s"%(self.name, self.restaraunt)






