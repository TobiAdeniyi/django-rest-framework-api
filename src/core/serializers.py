from rest_framework import serializers
from core.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'weight', 'color', 'euler_char']
