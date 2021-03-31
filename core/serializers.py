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
        fields = ['id', 'user', 'name', 'basket']

    def get_basket(self, instance):
        basket = Basket.objects.get(customer=instance)
        return BasketSerializer(basket, many=False).data


class BasketSerializer(serializers.ModelSerializer):
    basket_items = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['customer', 'date_added', 'basket_items']

    def get_basket_items(self, instance):
        basket_items = BasketItem.objects.filter(basket=instance)
        return BasketItemSerializer(basket_items, many=True).data


class BasketItemSerializer(serializers.ModelSerializer):
    quntity = serializers.IntegerField(min_value=1, max_value=100)

    class Meta:
        model = BasketItem
        fields = '__all__'
