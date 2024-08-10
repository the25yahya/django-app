from django.shortcuts import render,redirect
from .models import Personal,Tokens
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.urls import reverse 
import json

# Create your views here.
@csrf_exempt
def userProfile(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        access_token = body.get('access_token')
        print('body: ',body)
        print('access token: ',access_token)
        try:
            token = Tokens.objects.get(access_token=access_token)
            user = token.user
        except Tokens.DoesNotExist:
            user = None
            print(access_token)
            print("no matching token found")
        if user is None:
            return JsonResponse({'error':'invalid token'},status=404)
        personal_context = {'user':user} 
        return render(request,'userProfile.html',personal_context)
    return JsonResponse({'error':'invalid request method'},status=405)

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
            'access_token': access_token,
            'refresh_token': refresh_token,
        })
    return JsonResponse({"detail": "Invalid method"}, status=405)