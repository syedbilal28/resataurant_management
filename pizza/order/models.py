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
    name = models.CharField(max_length=30,unique=True)
    contact = models.CharField(max_length=11,unique=True)
    password= models.CharField(max_length=30,default="password")
    def __str__(self):
        return self.name

class Order(models.Model):
    order_no = models.CharField(max_length=4)
    date_time = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    def __str__(self):
        return "{},{}, {}".format(self.order_no,self.pizza,self.customer)
class OrderQueue(models.Model):
    id = models.ForeignKey(Order, on_delete=models.CASCADE,primary_key=True,unique = True)

    def __str__(self):
        return "{}".format(str(self.id))
