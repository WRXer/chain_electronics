# Generated by Django 4.2.5 on 2023-10-07 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0009_alter_supply_partner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supply',
            name='products',
        ),
    ]
