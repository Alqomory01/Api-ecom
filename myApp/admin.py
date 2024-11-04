from django.contrib import admin
from .models import Categorie, Brand, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    ordering = ['name']
    list_per_page = True
    search_fields = ['name']

class  BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profile']
    list_filter = ['name']
    ordering = ['created_at']
    search_fields = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'category', 'brand', 'price']
    list_filter = ['category']
    ordering = ['price']

# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ['id', 'product']



 
# admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Categorie, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)


# Register your models here.
