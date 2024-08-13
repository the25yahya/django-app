# home/urls.py
from django.urls import path
from .views import home, newArrivals,login,signup,sunglasses,eyeglasses,shopCart,wishlist

urlpatterns = [
    path('', home, name='home'),
    path('newArrivals',newArrivals, name='newArrivals'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('sunglasses',sunglasses,name='sunglasses'),
    path('eyeglasses',eyeglasses,name='eyeglasses'),
    path('shopCart',shopCart,name='shopCart'),
    path('wishlist',wishlist,name='wishlist')
]
