from django.contrib import admin
from django import forms

from products.models import Partner
from supply.models import Supply


# Register your models here.
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'node_type', 'is_active')


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner', 'supplier', 'supplier_country', 'get_products_list', 'debt_to_supplier', 'release_date', 'is_active')
    readonly_fields = ('supplier_email', 'supplier_country')    #Добавляем readonly поля

    def get_products_list(self, obj):
        return ', '.join([product.name for product in obj.products.all()])

    def supplier_email(self, obj):
        return obj.supplier.email

    def supplier_country(self, obj):
        return obj.supplier.country

    supplier_email.short_description = 'Email поставщика'    #Название колонки
    supplier_country.short_description = 'Страна поставщика'
    get_products_list.short_description = 'Products'