from rest_framework import serializers
from .models import Supply, Partner


class SupplySerializer(serializers.ModelSerializer):
    """
    Сериализатор поставки
    """
    class Meta:
        model = Supply
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    """
    Сериализатор организации
    """
    class Meta:
        model = Partner
        fields = '__all__'