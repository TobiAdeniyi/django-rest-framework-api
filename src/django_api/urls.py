from django.contrib import admin
from django.urls import path, include

from core.views import TestView, ProductsList
# from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/', include(router.urls)),
    # path('', TestView.as_view(), name='test'),
    path('', ProductsList.as_view(), name='products'),
]
