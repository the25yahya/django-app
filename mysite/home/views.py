from django.shortcuts import render
from django.http import HttpResponse
from .models import home_sunglasses,new_arrivals,sun_glasses,eye_glasses

def home(request):
    context = {'name':'yahya'}
    list_sunglasses = home_sunglasses.objects.all()
    return render(request,'home.html',{'home_sunglasses':list_sunglasses,
                                       'context':context})

def newArrivals(request):
    list_newArrivals = new_arrivals.objects.all()
    return render(request,'newArrivals.html',{'newArrivals' : list_newArrivals})

def sunglasses(request):
    list_sunglasses = sun_glasses.objects.all()
    return render(request,'sunglasses.html',{'sunglasses': list_sunglasses})

def eyeglasses(request):
    list_eyeglasses = eye_glasses.objects.all()
    return render(request,'eyeglasses.html',{'eyeglasses': list_eyeglasses})

def shopCart(request):
    return render(request,'shopCart.html')

def wishlist(request):
    return render(request,'wishlist.html')

def signup(request):
    context = {}
    return render(request,'signup.html',context)

def login(request):
    return render(request,'login.html')

def search(request):
    query = request.GET.get('query','')
    results = []
    if query :
        results = new_arrivals.objects.filter(name=query)
    return render(request, 'search.html', {'results': results, 'query': query})