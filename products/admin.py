from django.contrib import admin
from products.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'manufacturer', 'is_active', 'author')
    exclude = ['author']


