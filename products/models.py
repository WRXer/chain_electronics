from django.db import models


# Create your models here.
class Product(models.Model):
    """
    Модель продукта
    """
    name = models.CharField(max_length=50, verbose_name='название продукта')
    model = models.CharField(max_length=50, verbose_name='модель продукта')
    release_date = models.DateField(auto_now_add=True, verbose_name='дата выхода продукта')
    is_active = models.BooleanField(default=True, verbose_name='активация продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = 'продукты'