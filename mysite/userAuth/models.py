from django.db import models
from userProfile.models import Personal

class Tokens(models.Model):
    id = models.AutoField(primary_key=True)
    access_token = models.CharField(max_length=500, null=False, blank=False)
    refresh_token = models.CharField(max_length=500, null=False, blank=False)
    user = models.ForeignKey(Personal, on_delete=models.CASCADE, null=False, blank=True, related_name='tokens')

    class Meta:
        db_table = 'tokens'