from django.db import models

class home_sunglasses(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=300)
    name = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'home_sunglasses'