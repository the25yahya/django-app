from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def userProfile(request):
    email = 'the25yahya@wearehackerone.com'
    try:
        user = UserProfile.objects.get(email=email)
    except UserProfile.DoesNotExist as error:
        print(f"user not found : {error}") 
    context = {'user':user}
    return render(request,'userProfile.html',context)