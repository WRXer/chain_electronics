from django.contrib import admin
from django import forms

from products.admin_filters import SupplierCityFilter, PartnerCityFilter
from products.models import Partner
from supply.models import Supply


# Register your models here.
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'node_type', 'is_active')


class SupplyAdminForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        supplier = cleaned_data.get('supplier')
        product = cleaned_data.get('product')
        partner = cleaned_data.get('partner')
        if supplier == partner:
            raise forms.ValidationError("Организация не может быть одновременно поставщиком и заказчиком.")
        if supplier.node_type == 'Завод':    #Проверяем, что организация-производитель совпадает с организацией в продукте, если тип поставщика завод
            if supplier != product.manufacturer:
                raise forms.ValidationError(
                    "Организация-производитель в заявке должна совпадать с организацией в продукте.")
        return cleaned_data


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    form = SupplyAdminForm
    list_display = ('id', 'partner', 'partner_city', 'supplier_link', 'supplier_city', 'product', 'debt_to_supplier', 'release_datetime', 'is_active')
    readonly_fields = ('supplier_email', 'supplier_city')    #Добавляем readonly поля
    list_filter = (SupplierCityFilter, PartnerCityFilter)    #Фильтр по городу
    actions = ['clear_debt']

    def supplier_link(self, obj):
        return obj.supplier.name

    def supplier_email(self, obj):
        return obj.supplier.email

    def supplier_city(self, obj):
        return obj.supplier.city

    def partner_city(self,obj):
        return obj.partner.city

    def clear_debt(self, request, queryset):
        """Функция очистки задолженности"""
        for network_object in queryset:
            network_object.debt_to_supplier = 0
            network_object.save()
        self.message_user(request, f'Задолженность перед поставщиком у выбранных объектов очищена.')

    supplier_link.short_description = 'Поставщик'
    supplier_link.admin_order_field = 'supplier__name'
    clear_debt.short_description = 'Очистить задолженность перед поставщиком'
    raw_id_fields = ('supplier',)
    partner_city.short_description = 'Город организации'
    supplier_email.short_description = 'Email поставщика'    #Название колонки
    supplier_city.short_description = 'Город поставщика'



