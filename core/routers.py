from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, CustomerBasketViewSet

router = DefaultRouter()

router.register('products', ProductsViewSet)
router.register('baskets', CustomerBasketViewSet)
# router.register('baskets/<str:customer_name>/', CustomerBasketViewSet)
