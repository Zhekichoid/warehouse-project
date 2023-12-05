from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=30)
    brand = models.CharField(max_length=20, default='n/a')
    product_type = models.CharField(max_length=40, default='n/a')
    initial_price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    final_price = models.DecimalField(max_digits=7, decimal_places=2)
# Create your models here.
