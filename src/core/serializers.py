from rest_framework import serializers
from .models import Products, Customers, Baskets


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baskets
        fields = '__all__'
