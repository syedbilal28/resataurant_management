from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.contrib.auth import login,authenticate,logout

from django.contrib.auth.models import User
# Create your views here.
def Menu(request):
    return render(request,"menu.html")
def Signup_page(request):
    return render(request,"signup.html")
def Login_page(request):
    return render(request,'login.html')
def SignUp(request):
    username = request.POST.get("customer_name",False)
    password = request.POST.get("password",False)

    number= request.POST.get("contact_number",False)
    user= User.objects.create_user(username=username,password=password)
    customer= Customer.objects.create(user=user,contact=number)
    user.save()
    customer.save()
    login(request,user)
    return render(request,"menu.html")
def Login(request):
    username= request.POST.get("customer_name",False)
    password = request.POST.get("password",False)
    print(password)
    user = authenticate(request,username=username,password=password)
    print(user)
    if user:
        print("logging in")
        login(request,user)
        return render(request,"menu.html")
    else:
        return render(request,"error.html")



def Logout(request):
    logout(request)
    return render(request,"menu.html")
# def customer_order(request):
#     orders = Order.objects.all(name= )