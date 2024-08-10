from django.shortcuts import render,redirect
from .models import Personal,Tokens
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.urls import reverse 
# Create your views here.
def userProfile(request):
    
    try:
        user = Personal.objects.get(email=email)
    except Personal.DoesNotExist as error:
        print(f"user not found : {error}") 
    context = {'user':user}
    return render(request,'userProfile.html',context)


@csrf_exempt
def register(request):
    if request.method == 'POST':

        #get data from post request
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        personal = Personal.objects.create(
           full_name= full_name,
           email=email,
           password = password
        )

                # Generate JWT tokens
        refresh = RefreshToken.for_user(personal)  
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        Tokens.objects.create(
            user=personal,  # Associate the token with the personal entry
            access_token=access_token,
            refresh_token=refresh_token
        )

        return JsonResponse({
            'access': access_token,
            'refresh': refresh_token,
        })
    return JsonResponse({"detail": "Invalid method"}, status=405)