from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {'name':'yahya'}
    return render(request,'home.html',context)