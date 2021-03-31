from django.urls import path, include
from .views import  (
    ProductListCreate, ProductRetrieveUpdateDestroyAPIView, 
    BasketListCreate, BasketRetrieveUpdateDelete,
    CustomerListCreate, CustomerRetrieveUpdateDelete,
)


urlpatterns = [
    path('products', ProductListCreate.as_view()),
    path('products/<int:id>', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('baskets', BasketListCreate.as_view()),
    path('baskets/<int:id>', BasketRetrieveUpdateDelete.as_view()),
    path('customer', CustomerListCreate.as_view()),
    path('customer/<int:id>', CustomerRetrieveUpdateDelete.as_view()),
]
