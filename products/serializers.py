from rest_framework import serializers
from .models import Product
from .validators import ManufacturerValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model', 'manufacturer']
        validators = [ManufacturerValidator()]

