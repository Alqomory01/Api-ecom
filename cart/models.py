from django.db import models
from myApp.models import Product
from customer.models import Customer

class Cart(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(item.total for item in self.cart_items.all())
    
class CartItem(models.Model):
        cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)
        created_at = models.DateTimeField(auto_now_add=True)

        @property
        def total(self):
            if self.product:
                return self.product.price * self .quantity
            return 0.0
        
        def __str__(self):
            return f"{self.product.name} (Qty {self.quantity})"
        
        class Meta:
            ordering = ['-created_at']

# Create your models here.
