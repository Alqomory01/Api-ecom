from rest_framework import serializers
from .models import Categorie, Brand, Product, CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
        read_only = ('id')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']
        read_only = ('id')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']
        read_only = ('id')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',  'category', 'brand']