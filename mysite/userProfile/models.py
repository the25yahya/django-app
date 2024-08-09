from django.db import models


class UserProfile(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField()
    home_town = models.CharField(max_length=50)

    class Meta:
        db_table = 'personal'
