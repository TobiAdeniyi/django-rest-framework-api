from django.http import JsonResponse
from django.shortcuts import render

# 3rd Party Imports
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {'name': 'Dave', 'age': 25}
        return Response(data)
