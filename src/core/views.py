from rest_framework import viewsets, filters
from rest_framework.response import Response

# Import modules
from .models import Products
from .serializers import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    Admin viewer:
    * View all products in store
    * Create a new products in store
    * Delete all products in store
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
