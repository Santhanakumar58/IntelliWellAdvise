from django.urls import path
from django.contrib.auth import views as auth
from django.urls import path
from Home import views


urlpatterns = [
    path("", views.homeindex, name="index"),
    path("backend/", views.backend, name="backend"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),  
    path("signup", views.signup, name="signup"),  
    path("signin", views.signin, name="signin"),     
    path("signout", views.signout, name="signout"),  
    path("leftsidenavi", views.leftsidenavi, name="leftsidenavi"), 
    path("topandside", views.topandside, name="topandside"), 
    path("lefttop1", views.lefttop1, name="lefttop1"), 


]