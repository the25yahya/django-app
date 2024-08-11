# home/urls.py
from django.urls import path
from .views import home, newArrivals,login,signup

urlpatterns = [
    path('', home, name='home'),
    path('newArrivals',newArrivals, name='newArrivals'),
    path('login',login,name='login'),
    path('signup',signup,name='signup')
]
