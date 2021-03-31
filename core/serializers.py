from rest_framework import serializers
from .models import Product, Customer, Basket, BasketItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    basket = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'name', 'basket']

    def get_basket(self, instance):
        basket = Basket.objects.filter(customer=instance)
        return BasketSerializer(basket, many=True).data


class BasketSerializer(serializers.ModelSerializer):
    basket_items = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['id', 'basket_items']

    def get_basket_items(self, instance):
        basket_items = BasketItem.objects.filter(basket=instance)
        return BasketItemSerializer(basket_items, many=True).data


class BasketItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = BasketItem
        fields = ['product', 'quantity', 'date_added']
