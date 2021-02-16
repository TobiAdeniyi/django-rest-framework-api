from django.http import Http404

# 3rd Party Imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Model imports
from core.models import Products
from core.serializers import ProductSerializers


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {'name': 'Dave', 'age': 25}
        return Response(data)


class ProductsList(APIView):
    """
    View to list all products in the stored
    """

    def get(self, request, format=None):
        """
        Returns a list of all products
        """
        products = []
