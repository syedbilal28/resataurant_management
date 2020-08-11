from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pizza(models.Model):
    Flavor = models.CharField(max_length = 20)
    # size = models.CharField(max_length=10)
    # toppings= models.IntegerField()
    # quantity=models.IntegerField()
    def __str__(self):
        return " Flavor: {}".format(self.Flavor)
class Toppings(models.Model):
    topping= models.CharField(max_length=256)
    def __str__(self):
        return self.topping

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=11,unique=True)

class Item(models.Model):
    pizza= models.ForeignKey(Pizza,on_delete=models.CASCADE)
    size= models.CharField(max_length=256,choices=[('Large','Large'),('Medium','Medium'),('Small','Small')])
    quantity= models.IntegerField()
    topping= models.OneToOneField(Toppings,on_delete=models.CASCADE)


class Order(models.Model):

    date_time = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Items = models.ForeignKey(Item,on_delete=models.CASCADE,default=False)
    def __str__(self):
        return "{},{}".format(self.pk,self.customer)
class OrderQueue(models.Model):
    id = models.OneToOneField(Order, on_delete=models.CASCADE,primary_key=True,unique = True)

    def __str__(self):
        return "{}".format(str(self.id))
