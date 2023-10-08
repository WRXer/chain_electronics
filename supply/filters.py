import django_filters
from .models import Supply

class SupplyFilter(django_filters.rest_framework.FilterSet):
    """
    Фильтрация по стране
    """
    supplier_country = django_filters.CharFilter(field_name='supplier__country', lookup_expr='iexact')    #Фильтрация поставщика
    partner_country = django_filters.CharFilter(field_name='partner__country', lookup_expr='iexact')    #Фильтрация организации
    class Meta:
        model = Supply
        fields = ['supplier_country', 'partner_country']