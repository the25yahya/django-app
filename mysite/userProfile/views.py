from django.shortcuts import render,redirect
from userAuth.models import Tokens
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse 
import json


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
                elif tab == 'payment':
                    return render(request,'payment.html',personal_context)
                elif tab == 'login':
                    return render(request,'loginInfo.html',personal_context)
                return render(request,'userProfile.html',personal_context)

    return JsonResponse({'error':'invalid request method'},status=405)


