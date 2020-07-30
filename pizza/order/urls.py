from django.urls import path
from . import views

urlpatterns=[
    path("",views.Menu,name = "Menu"),
    path("login",views.Login_page,name="Login_page"),
    path("Login",views.Login,name="Login"),
    path("signup",views.Signup_page,name="Signup_page"),
    path("Signup",views.SignUp,name="Signup"),
    path("logout",views.Logout,name="Logout")

]
