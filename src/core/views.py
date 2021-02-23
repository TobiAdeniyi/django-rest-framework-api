from django.http import Http404

# 3rd Party Imports
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
# from rest_framework.decorators import action

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

    # # GET - Order by
    # @action(methods=['GET'], detail=False)
    # def organised(self, request):
    #     ordered = self.get_queryset().order_by('name')
    #     serializer = self.get_serializer_class()(ordered, many=True)
    #     return Response(serializer.data)
