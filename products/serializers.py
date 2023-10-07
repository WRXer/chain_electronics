from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'model', 'manufacturer']

    def validate(self, data):
        """
        Валидация продукта
        """
        node_type = self.context.get('request').data.get('node_type')    #Получаем тип звена организации из переданного запроса (если это доступно)
        if node_type != 'Завод':    #Проверяем, является ли организация заводом
            raise serializers.ValidationError("Только заводы могут создавать продукты.")
        return data