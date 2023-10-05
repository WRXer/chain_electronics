from django.contrib import admin
from products.models import Partner
from supply.models import Supply


# Register your models here.
@admin.register(Partner)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'node_type', 'is_active')


@admin.register(Supply)
class UserAdmin(admin.ModelAdmin):
    list_display = ('partner', 'supplier', 'get_products_list', 'debt_to_supplier', 'release_date', 'is_active')

    def get_products_list(self, obj):
        return ', '.join([product.name for product in obj.products.all()])

    get_products_list.short_description = 'Products'