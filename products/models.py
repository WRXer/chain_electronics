from django.db import models
from django.conf import settings

from supply.models import Partner


# Create your models here.
class Product(models.Model):
    """
    Модель продукта
    """
    name = models.CharField(max_length=50, verbose_name='Название продукта')
    model = models.CharField(max_length=50, verbose_name='Модель продукта')
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата выхода продукта')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    is_active = models.BooleanField(default=True, verbose_name='Активация продукта')
    manufacturer = models.ForeignKey(Partner, on_delete=models.CASCADE, limit_choices_to={'node_type': 'Завод'}, verbose_name='Организация производитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'