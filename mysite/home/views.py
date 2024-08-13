from django.shortcuts import render
from django.http import HttpResponse
from .models import home_sunglasses

def home(request):
    context = {'name':'yahya'}
    list_sunglasses = home_sunglasses.objects.all()
    return render(request,'home.html',{'home_sunglasses':list_sunglasses,
                                       'context':context})

def newArrivals(request):
    return render(request,'newArrivals.html')

def sunglasses(request):
    return render(request,'sunglasses.html')

def eyeglasses(request):
    return render(request,'eyeglasses.html')

def shopCart(request):
    return render(request,'shopCart.html')

def wishlist(request):
    return render(request,'wishlist.html')

def signup(request):
    context = {}
    return render(request,'signup.html',context)

def login(request):
    return render(request,'login.html')
