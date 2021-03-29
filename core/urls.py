from django.urls import path, include
from .views import ProductList, ProductCreate, ProductRetrieveUpdateDestroyAPIView, BasketList


urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/new', ProductCreate.as_view()),
    path('products/<int:id>', ProductRetrieveUpdateDestroyAPIView.as_view()),
]
