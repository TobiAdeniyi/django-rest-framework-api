from django.http import Http404

# 3rd Party Imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Import modules
from .models import Products
from .serializers import ProductSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {'name': 'Dave', 'age': 25}
        return Response(data)


class ProductsList(APIView):
    """
    Admin viewer:
    * View all products in store
    * Create a new products in store
    * Delete all products in store
    """

    # GET - Retrive all resorces
    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # POST - Create new resource
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE - Detroy all resource
    def delete(self, request, format=None):
        products = Products.objects.all()
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
