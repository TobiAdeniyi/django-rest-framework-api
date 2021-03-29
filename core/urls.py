from django.urls import path, include
from .views import ProductList, ProductCreate, ProductDestroy, BasketList


urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/new', ProductCreate.as_view()),
    path('products/<int:id>/destroy', ProductDestroy.as_view()),
]
