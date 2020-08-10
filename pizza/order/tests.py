from django.test import TestCase,Client
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate

# Create your tests here.
class OrderTest(TestCase):
    def setUp(self):
        # Creating user and Customer
        self.user= User.objects.create_user(username="be red",password="123456")
        customer= Customer.objects.create(user=self.user,contact="11111")
    def test1(self):

        user= authenticate(username="be red",password="123456")
        self.assertEqual(user,self.user)
        # print(user)
        #
        # login(request,user=user)
    def test2(self):
        customers= Customer.objects.all()



