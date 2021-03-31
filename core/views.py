from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from .serializers import ProductSerializer, CustomerSerializer,  BasketSerializer, BasketItemSerializer
from .models import Product, Customer, Basket, BasketItem


class ProductsPagination(LimitOffsetPagination):
    """
    Defualt and Maximum number of pages
    """
    default_limit = 10
    max_limit = 100


class ProductListCreate(ListCreateAPIView):
    """
    All view:
    * View all products in store
    * Create new product in store
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsPagination
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'weight', 'color']
    ordering_fields = ['name', 'weight', 'color']
    search_fields = ['name', 'weight', 'color']

    # Ensure input data is suitable
    def create(self, request, *args, **kwargs):
        try:
            weight = request.data.get('weight')
            if weight is not None and float(weight) <= 0.0:
                raise ValidationError({'weight': 'Must be above 0kg'})
        except ValueError:
            raise ValidationError({'weight': 'A valid weight is required'})
        return super().create(request, *args, **kwargs)


class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Admin view:
    * Rtrieve a given product
    * Update a given product
    * Destroy a given product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    # Delete cache of deleted product
    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    # Update data and cache
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            serializer = ProductSerializer(data=product)
            cache.set('product_data_{}'.format(product['id']), serializer)
        return response


class CustomerListCreate(ListCreateAPIView):
    """
    Customer viewer:
    * List products in basket
    * Add product to basket
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'

    # Create a basket item
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CustomerRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Customer viewer:
    * Retrieve detail on a product in basket
    * Update detail of the number of a product in basket
    * Delete a product from basket
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'


class BasketListCreate(ListCreateAPIView):
    """
    Admin viewer:
    * View all baskets of customers
    * Create a new basket for customer
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'

    # Create a basket item
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class BasketRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    Admin viewer:
    * Retrieve a given user basket
    * Update a given user basket
    * Delete a given user basket
    """
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    lookup_field = 'id'


class BasketItemListCreate(ListCreateAPIView):
    """
    Admin viewer:
    * View all baskets of customers
    * Create a new basket for customer
    """
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'

    # Create a basket item
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
