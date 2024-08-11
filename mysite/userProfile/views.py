from django.shortcuts import render,redirect
from .models import Personal,Tokens
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.urls import reverse 
import json
from django.contrib.auth.hashers import check_password


@csrf_exempt
def userProfile(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        access_token = body.get('access_token')
        try:
            token = Tokens.objects.get(access_token=access_token)
            user = token.user
        except Tokens.DoesNotExist:
            user = None
            print("no matching token found")
        if user is None:
            return JsonResponse({'error':'invalid token'},status=404)
        personal_context = {'user':user} 
        return render(request,'userProfile.html',personal_context)
    if request.method == 'GET':
            tab = request.GET.get('tab',None)
            access_token = request.COOKIES.get('access_token')
            refresh_token = request.COOKIES.get('refresh_token')
            if access_token and refresh_token :
                try:
                    token = Tokens.objects.get(access_token=access_token)
                    user = token.user
                except Tokens.DoesNotExist:
                    user = None
                if user is None:
                    return JsonResponse({'error':'invalid token'},status=404)
                personal_context = {'user':user} 
                print(tab)
                if tab == 'personal':
                    return render(request,'userProfile.html',personal_context)
                elif tab == 'settings':
                    print('returning : settings.html')
                    return render(request,'settings.html',personal_context)
                elif tab == 'payement':
                    return render(request,'payement.html',personal_context)
                elif tab == 'login':
                    return render(request,'loginInfo.html',personal_context)
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

@csrf_exempt
def login(request):
    if request.method == 'POST':
        # Get data from POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Fetch the personal entry with the provided email
            personal = Personal.objects.get(email=email)
            # Check if the password is correct
            if password == personal.password:
                # Generate JWT tokens
                refresh = RefreshToken.for_user(personal)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                # Create or update the tokens in the Tokens model
                Tokens.objects.update_or_create(
                    user=personal,
                    defaults={
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }
                )

                return JsonResponse({
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                })
            else:
                return JsonResponse({"detail": "Invalid email or password"}, status=401)

        except Personal.DoesNotExist:
            return JsonResponse({"detail": "Invalid email or password"}, status=401)

    return JsonResponse({"detail": "Invalid method"}, status=405)

@csrf_exempt
def testLogin(request):
    if request.method == 'POST':
        # Get data from POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Fetch the personal entry with the provided email
        personal = Personal.objects.get(email=email)
        print(personal)
        if personal:
            return JsonResponse({'name':personal.full_name,
                                 'email':personal.email,
                                 'password':personal.password})