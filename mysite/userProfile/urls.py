from django.urls import path
from .views import userProfile,profile_upload


urlpatterns = [
    path('',userProfile,name='userProfile'),
    path('/profileUpload',profile_upload,name='profileUpload'),
]