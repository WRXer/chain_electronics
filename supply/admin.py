from django.contrib import admin
from django import forms

from products.admin_filters import SupplierCityFilter, PartnerCityFilter
from products.models import Partner
from supply.models import Supply


# Register your models here.
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'node_type', 'is_active')


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner', 'partner_city', 'supplier_link', 'supplier_city', 'get_products_list', 'debt_to_supplier', 'release_datetime', 'is_active')
    readonly_fields = ('supplier_email', 'supplier_city')    #Добавляем readonly поля
    list_filter = (SupplierCityFilter, PartnerCityFilter)    #Фильтр по городу

    def supplier_link(self, obj):
        return obj.supplier.name

    supplier_link.short_description = 'Поставщик'
    supplier_link.admin_order_field = 'supplier__name'

    def get_products_list(self, obj):
        return ', '.join([product.name for product in obj.products.all()])

    def supplier_email(self, obj):
        return obj.supplier.email

    def supplier_city(self, obj):
        return obj.supplier.city

    def partner_city(self,obj):
        return obj.partner.city

    raw_id_fields = ('supplier',)
    partner_city.short_description = 'Город организации'
    supplier_email.short_description = 'Email поставщика'    #Название колонки
    supplier_city.short_description = 'Город поставщика'
    get_products_list.short_description = 'Products'


