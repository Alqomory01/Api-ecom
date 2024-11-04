from rest_framework import serializers
from .models import Categorie, Brand, Product, ProductImages

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['product', 'quantity']
#         read_only = ('id')

    



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'name']
        read_only = ('id')

    def create(self, validate_data):
        return Categorie.objects.create(**validate_data)
    
    def update(self, instance, validate_data): 
        instance.name = validate_data.get('name', instance.name)
        instance.save()
        return instance

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'profile' ]
        read_only = ('id')

    def create (self, validate_data):
        return Brand.objects.create(**validate_data)  

    def update(self, instance, validate_data):  
        instance.name = validate_data.get('name', instance.name)
        instance.profile = validate_data.get('profile', instance.profile)
        instance.save()
        return instance

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']

    def create (self, validate_data):
        return Product.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.image = validate_data.get('image', instance.image)
        instance.save()
        return instance
    
class ProductSerilizer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(slug_field='name', queryset=Brand.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Categorie.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'description', 'price', 'quantity', 'brand', 'category', 'image']

    def create(self, validated_model):
        return Product.objects.create(**validated_model)
    
    def update(self, instance, validated_model):
        instance.name = validated_model.get('name', instance.name)
        instance.description = validated_model.get('description', instance.description)
        instance.price = validated_model.get('price', instance.price)
        instance.quantity = validated_model.get('quantity', instance.quantity)
        instance.brand = validated_model.get('brand', instance.brand)
        instance.category = validated_model.get('category', instance.category)
        instance.save()
        return instance
