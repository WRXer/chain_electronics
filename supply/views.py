from rest_framework import viewsets

from .filters import SupplyFilter
from .models import Supply, Partner
from .permissions import CustomAccessPermission
from .serializers import SupplySerializer, PartnerSerializer


# Create your views here.
class SupplyViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с поставками.
    """
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    permission_classes = [CustomAccessPermission]    #доступ
    filter_class = SupplyFilter    #фильтрация


class PartnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с партнерами.
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [CustomAccessPermission]
