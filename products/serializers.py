from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model', 'manufacturer']


    def validate_manufacturer(self, value):
        """
        Проверяем, является ли организация заводом
        """
        if value.node_type != 'Завод':
            raise serializers.ValidationError("Только заводы могут создавать продукты.")
        return value