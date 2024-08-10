from django.urls import path
from .views import userProfile,register



urlpatterns = [
    path('',userProfile,name='userProfile'),
    path('register',register,name='register')
]