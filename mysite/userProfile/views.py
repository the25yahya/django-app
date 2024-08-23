from django.shortcuts import render
from userAuth.models import Tokens
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.conf import settings
import os
from django.conf import settings
from .models import Personal



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




@csrf_exempt
def profile_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        user_id = request.POST.get('user_id')  # Assuming you send the user_id in the POST request
        
        # Define the path to the media directory
        media_root = os.path.join(settings.MEDIA_ROOT, 'profile_pics')
        
        # Create the directory if it doesn't exist
        if not os.path.exists(media_root):
            os.makedirs(media_root)
        
        # Create the full file path
        file_path = os.path.join(media_root, uploaded_file.name)
        
        # Save the uploaded file
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        
        # Update the Personal model with the filename
        try:
            # Get the user's Personal record
            personal = Personal.objects.get(id=user_id)
            personal.profile_pic = uploaded_file.name
            personal.save()

            return JsonResponse({
                'success': True,
                'new_img_url': f'/media/profile_pics/{uploaded_file.name}'
            })
        except Personal.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User not found'}, status=404)
    
    return JsonResponse({'success': False}, status=400)

