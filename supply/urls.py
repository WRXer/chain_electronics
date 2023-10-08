from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import SupplyConfig
from .views import SupplyViewSet, PartnerViewSet


app_name = SupplyConfig.name


router = DefaultRouter()
router.register(r'supplies', SupplyViewSet)
router.register(r'partners', PartnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]