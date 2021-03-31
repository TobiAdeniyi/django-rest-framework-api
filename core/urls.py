from django.urls import path, include
from .views import  (
    ProductListCreate, ProductRetrieveUpdateDestroy, 
    BasketListCreate, BasketRetrieveUpdateDestroy,
    CustomerListCreate, CustomerRetrieveUpdateDestroy,
)


urlpatterns = [
    path('products', ProductListCreate.as_view()),
    path('products/<int:id>', ProductRetrieveUpdateDestroy.as_view()),
    path('baskets', BasketListCreate.as_view()),
    path('baskets/<int:id>', BasketRetrieveUpdateDestroy.as_view()),
    path('customers', CustomerListCreate.as_view()),
    path('customers/<int:id>', CustomerRetrieveUpdateDestroy.as_view()),
]
