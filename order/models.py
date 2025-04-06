from django.db import models
from products.models import Product
from users.models import CustomUserModel
# Create your models here.
class Order(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_orders')
    count = models.IntegerField(default=0)
    owner = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='owner_orders')