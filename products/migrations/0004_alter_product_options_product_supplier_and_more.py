# Generated by Django 4.2.5 on 2023-10-05 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_product_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supply.partner', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активация продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Модель продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата выхода продукта'),
        ),
    ]