from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid

class Categorie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55)
    profile = models.ImageField(upload_to='product_image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Categorie,  on_delete=models.CASCADE)
    product = models.CharField(max_length=55)
    brand = models.ForeignKey(Brand,  on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='product_image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.product
    
# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

#     @property
#     def total(self):
#         return self.product.price * self.quantity
    
#     def __str__(self):
#         return  self.product.product
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)


# Create your models here.
