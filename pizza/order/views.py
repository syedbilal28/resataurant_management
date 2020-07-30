from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.contrib.auth import login,authenticate,logout

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
    number= request.POST.get("contact",False)
    customer= Customer(name=username,password=password,contact=number)
    login(request,customer)
    return render(request,"menu.html")
def Login(request):
    username= request.POST.get("username",False)
    password = request.POST.get("password",False)
    user = authenticate(request,username =username,password= password)
    if user is not None:
        login(request,user)
        return render(request,"menu.html")
def Logout(request):
    logout(request)
    return render(request,"menu.html")
# def customer_order(request):
#     orders = Order.objects.all(name= )