from rest_framework import serializers
from .models import *

# Get serializers
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']

class CartItemSerializers(serializers.ModelSerializers):
    cart = CartSerializer
    class Meta:
        model = CartItem
        field = ['cart', 'product', 'quantity']

# post serializers
class CreateCartItemSeriazer(serializers.ModelSerializers):
    cart = serializers.SlugField(slug_field="id", queryset=Cart.objects.all())
    product = serializers.SlugField(slug_field="name", queryset=Product.objects.all())

    class Meta:
            model = CartItem
            fields = ['cart', 'product', 'quantity']

    def create(self, validated_at):
        return CartItem.objects.create(**validated_at)
    
    def update(self, instance, validated_model):
        instance.name = validated_model.get('name', instance.name)
        instance.quantity = validated_model.get('quantity', instance.quantity)
        instance.save()
        return instance