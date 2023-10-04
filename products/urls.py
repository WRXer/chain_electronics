from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import ProductsConfig
from .views import ProductViewSet


app_name=ProductsConfig.name

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
]