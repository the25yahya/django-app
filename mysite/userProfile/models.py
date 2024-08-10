from django.db import models
from django.contrib.auth.models import User

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    home_town = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=20, null=False, blank=False)  # Added password field

    class Meta:
        db_table = 'personal'



class Tokens(models.Model):
    id = models.AutoField(primary_key=True)
    access_token = models.CharField(max_length=500, null=False, blank=False)
    refresh_token = models.CharField(max_length=500, null=False, blank=False)
    user = models.ForeignKey(Personal, on_delete=models.CASCADE, null=True, blank=True, related_name='tokens')

    class Meta:
        db_table = 'tokens'