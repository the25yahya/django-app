from django.shortcuts import render

# Create your views here.
def userProfile(request):
    context = {'full-name':'yahya'}
    return render(request,'userProfile.html',context)