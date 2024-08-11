# home/urls.py
from django.urls import path
from .views import home, newArrivals

urlpatterns = [
    path('', home, name='home'),
    path('newArrivals',newArrivals, name='newArrivals')
]
