from .models import Customer
from django.http import HttpResponse
def authenticate(username,password):
    try:
        user= Customer.objects.get(name=username)
    except:
        return HttpResponse("User not registered")
    if user.password == password:
        return True
    return False