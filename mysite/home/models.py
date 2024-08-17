from django.db import models


class ProductDisplay(models.Model):
    img = models.CharField(max_length=300, blank=True, null=True)
    img2 = models.CharField(max_length=300, blank=True, null=True)
    img3 = models.CharField(max_length=300, blank=True, null=True)
    img4 = models.CharField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    brand = models.CharField(max_length=20, blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'product_display'

class home_sunglasses(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=300)
    name = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'home_sunglasses'

class new_arrivals(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=300)
    name = models.CharField(max_length=20,null=False)
    price = models.IntegerField(null=False)
    product = models.ForeignKey(ProductDisplay, on_delete=models.CASCADE, related_name='new_arrivals')

    class Meta:
        db_table = 'newArrivals'

class sun_glasses(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=300)
    name = models.CharField(max_length=20,null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'sunglasses'

class eye_glasses(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=300)
    name = models.CharField(max_length=20,null=False)
    price = models.IntegerField(null=False)

    class Meta:
        db_table = 'eyeglasses'

from django.db import models


class ShopCart(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductDisplay, on_delete=models.CASCADE)

    class Meta:
        db_table = 'shopcart'

class wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductDisplay, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wishlist'