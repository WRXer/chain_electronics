from django.db import models

# Create your models here.
class Partner(models.Model):
    """
    Организация, данные
    """
    FACTORY = 'Завод'
    RETAIL_NETWORK = 'Розничная сеть'
    ENTREPRENEUR = 'ИП'

    NODE_NAME_CHOICES = [
        (FACTORY, 'Завод'),
        (RETAIL_NETWORK, 'Розничная сеть'),
        (ENTREPRENEUR, 'ИП'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=55, verbose_name='Страна')
    city = models.CharField(max_length=55, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=20, verbose_name='Номер дома')
    node_type = models.CharField(max_length=255, choices=NODE_NAME_CHOICES, verbose_name='Тип звена')
    is_active= models.BooleanField(default=True, verbose_name='Актив организации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Supply(models.Model):
    """
    Поставка
    """
    partner = models.ForeignKey('Partner', on_delete=models.CASCADE, limit_choices_to={'node_type__in': ['ИП', 'Розничная сеть']}, related_name='partner', verbose_name='Организация')
    supplier = models.ForeignKey('Partner', on_delete=models.CASCADE,related_name='supplier', verbose_name='Поставщик')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='products', blank=True, verbose_name='Продукты')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность перед поставщиком')
    release_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заявки', null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активность заявки')

    def __str__(self):
        return f"Поставка для {self.partner.name}"

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'