from django.test import TestCase

# Create your tests here.
from core.models import Products
from core.serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Products(name='Shoe', weight=10, color='red', euler_char=1)
snippet.save()

snippet = Products(name='bag', weight=23, color='black', euler_char=2)
snippet.save()

snippet = Products(name='hat', weight=19, color='yellow', euler_char=2)
snippet.save()
