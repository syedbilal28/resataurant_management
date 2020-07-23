from django.db import models

# Create your models here.
class Pizza(models.Model):
    Flavor = models.CharField(max_length = 20)
    size = models.CharField(max_length=10)
    toppings= models.IntegerField()
    quantity=models.IntegerField()
    def __str__(self):
        return " Flavor: {}, Size: {}".format(self.Flavor,self.size)


class Customer(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=11)

class Order(models.Model):
    order_no = models.CharField(max_length=4)
    date_time = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
