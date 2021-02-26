from rest_framework import viewsets, filters, authentication, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

# Import modules
from .models import Product, Customer, Basket
from .serializers import BasketSerializer, ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    Admin viewer:
    * View all products in store
    * Create a new products in store
    * Delete all products in store
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'


class CustomerBasketViewSet(viewsets.ModelViewSet):
    """
    Customer viewer:
    * View all products in store
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
