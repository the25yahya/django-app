from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userProfile.models import Personal
from .models import Tokens
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password

# Create your views here.
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