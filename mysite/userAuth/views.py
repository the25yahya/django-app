from django.shortcuts import render

# Create your views here.
def signup(request):
    context = {}
    return render(request,'signup.html',context)