from rest_framework import serializers
from .models import Supply, Partner
from .validators import SupplierValidator, PartnerValidator


class SupplySerializer(serializers.ModelSerializer):
    """
    Сериализатор поставки
    """
    class Meta:
        model = Supply
        fields = '__all__'
        validators = [SupplierValidator(),
                      PartnerValidator()]

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        request = context.get('request')    # Извлекаем данные о запросе
        if request and request.method == 'POST':    # Если это запрос на создание, разрешаем изменение debt_to_supplier
            self.fields['debt_to_supplier'].read_only = False
        else:
            self.fields['debt_to_supplier'].read_only = True    #В остальных случаях (PUT, PATCH и т.д.) делаем debt_to_supplier доступным только для чтения
        super().__init__(*args, **kwargs)

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