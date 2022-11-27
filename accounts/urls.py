from django.contrib.auth.models import User
from django.urls import path
from .views import home,login,nowyou

urlpatterns = [
    path('',home, name= "home"),
    path('login/',login, name = "login"),
    path('nowyou/', nowyou, name =  "nowyou"),
   ]