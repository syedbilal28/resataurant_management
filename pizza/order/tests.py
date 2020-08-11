from django.test import TestCase,Client
from .models import Customer,Pizza,Item,Order,Toppings
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
import datetime
# Create your tests here.
class OrderTest(TestCase):
    def setUp(self):
        # Creating user and Customer
        self.user= User.objects.create_user(username="be red",password="123456")
        self.customer= Customer.objects.create(user=self.user,contact="11111")
    def test1(self):

        user= authenticate(username="be red",password="123456")
        self.assertEqual(user,self.user)
        # print(user)
        #
        # login(request,user=user)
    def test2(self):
        customers= Customer.objects.all()
    def test3(self):
        Flavor = "Sicilan Cheese"
        Flavor = Pizza.objects.create(Flavor=Flavor)
        t1= Toppings.objects.create(topping="Jalapeno")
        I1= Item.objects.create(pizza=Flavor,size="Large",quantity=1,topping=t1)
        O1= Order.objects.create(customer=self.customer,date_time=datetime.datetime.now(),Items=I1)
        self.assertEqual(O1.pk,1)




