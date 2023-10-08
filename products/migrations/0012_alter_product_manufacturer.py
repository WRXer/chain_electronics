# Generated by Django 4.2.5 on 2023-10-07 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0012_alter_supply_product'),
        ('products', '0011_alter_product_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(limit_choices_to={'node_type': 'Завод'}, on_delete=django.db.models.deletion.CASCADE, to='supply.partner', verbose_name='Организация производитель'),
        ),
    ]
