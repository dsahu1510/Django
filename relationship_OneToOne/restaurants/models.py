from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return '%s is the Name Of Place'% self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete = models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return '%s is the Restaurant '% self.place.name

# here in this example we cn simply that 2 restaurant cannot have same name.
# as it is one to one relationship. 

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s is the waiter from %s'%(self.name, self.restaurant)

# Here in this example one restaurant can have multiple waiters, nd this is one to many