"""
Router needs to be used for
- Read on how routers are used
- Implement appropriatly
"""
from rest_framework import routers
from core import views

router = routers.DefaultRouter()

router.register('test', views.TestView.as_view())
router.register('products', views.ProductsList.as_view())
