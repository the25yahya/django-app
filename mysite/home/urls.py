# home/urls.py
from django.urls import path
from .views import home, product, newArrivals,login,signup,sunglasses,eyeglasses,shopCart,wishlist,search,collections

urlpatterns = [
    path('', home, name='home'),
    path('newArrivals',newArrivals, name='newArrivals'),
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('sunglasses',sunglasses,name='sunglasses'),
    path('eyeglasses',eyeglasses,name='eyeglasses'),
    path('collections',collections,name='collections'),
    path('shopCart',shopCart,name='shopCart'),
    path('wishlist',wishlist,name='wishlist'),
    path('search', search, name='search'),
    path('product',product,name='product')
]
