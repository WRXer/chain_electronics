from rest_framework import serializers
from .models import Supply, Partner


class SupplySerializer(serializers.ModelSerializer):
    """
    Сериализатор поставки
    """
    class Meta:
        model = Supply
        fields = '__all__'

    def create(self, validated_data):
        validated_data['is_active'] = True  # Устанавливаем is_active в явное значение
        return super().create(validated_data)


class PartnerSerializer(serializers.ModelSerializer):
    """
    Сериализатор организации
    """
    class Meta:
        model = Partner
        fields = '__all__'