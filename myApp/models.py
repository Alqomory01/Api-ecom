from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categorie,  on_delete=models.CASCADE)
    product = models.CharField(max_length=55)
    brand = models.ForeignKey(Brand,  on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='product_image', blank=True, null=True)

    def __str__(self):
        return self.product
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    @property
    def total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return  self.product.product

# Create your models here.
