from rest_framework import viewsets
from rest_framework import permissions
from .models import Supply, Partner
from .serializers import SupplySerializer, PartnerSerializer


# Create your views here.
class SupplyViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с поставками.
    """
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class PartnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с партнерами.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
