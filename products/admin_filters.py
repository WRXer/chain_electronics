from django.contrib import admin
from supply.models import Partner


class SupplierCityFilter(admin.SimpleListFilter):
    """
    Фильтр по городу поставщика
    """
    title = 'Город поставщика'
    parameter_name = 'supplier_city'

    def lookups(self, request, model_admin):
        """
        Вернули значения для отображения в выпадающем списке
        """
        cities = Partner.objects.values_list('city', flat=True).distinct()
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        """
        Примените фильтр к queryset
        """
        city = self.value()
        if city:
            return queryset.filter(supplier__city=city)

class PartnerCityFilter(admin.SimpleListFilter):
    """
    Фильтр по городу организации
    """
    title = 'Город организации'
    parameter_name = 'partner_city'

    def lookups(self, request, model_admin):
        """
        Вернули значения для отображения в выпадающем списке
        """
        cities = Partner.objects.values_list('city', flat=True).distinct()
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        """
        Примените фильтр к queryset
        """
        city = self.value()
        if city:
            return queryset.filter(partner__city=city)