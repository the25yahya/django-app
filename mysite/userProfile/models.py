from django.db import models

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    home_town = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=20, null=False, blank=False)
    profile_pic = models.CharField(max_length=30)  # Added password field

    class Meta:
        db_table = 'personal'


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

