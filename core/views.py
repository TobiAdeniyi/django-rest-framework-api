from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from .serializers import ProductSerializer, BasketSerializer
from .models import Product, Basket


class ProductsPagination(LimitOffsetPagination):
    """
    Defualt and Maximum number of pages
    """
    default_limit = 10
    max_limit = 100


class ProductList(ListAPIView):
    """
    * View all products in store
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'weight', 'color']
    ordering_fields = ['name', 'weight', 'color']
    search_fields = ['name', 'weight', 'color']


class ProductCreate(CreateAPIView):
    """
    * Create new product in store
    """
    serializer_class = ProductSerializer
    # Ensure input data is suitable
    def create(self, request, *args, **kwargs):
        try:
            weight = request.data.get('weight')
            if weight is not None and float(weight) <= 0.0:
                raise ValidationError({'weight': 'Must be above 0kg'})
        except ValueError:
            raise ValidationError({'weight': 'A valid weight is required'})
        return super().create(request, *args, **kwargs)


class ProductDestroy(DestroyAPIView):
    """
    * Destroy a given product
    """
    queryset = Product.objects.all()
    lookup_field = 'id'
    # Delete cache of deleted product
    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response


class BasketList(ListAPIView):
    """
    Customer viewer:
    * View all products in store
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
