from django.urls import path
from .views import newArrivals


urlpatterns = [
    path('',newArrivals,name='newArrivals')
]