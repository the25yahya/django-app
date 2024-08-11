from django.urls import path
from .views import userProfile,register,login,testLogin



urlpatterns = [
    path('',userProfile,name='userProfile'),
    path('register',register,name='register'),
    path('login',login,name='login')
]