from django.contrib import admin
from products.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'manufacturer', 'is_active', 'author')
    exclude = ['author']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user    #Если объект создается, а не редактируется, устанавливаем автора
        super().save_model(request, obj, form, change)


