from django.shortcuts import render

def newArrivals(request):
    context = {}
    return render(request,'newArrivals.html',context)
