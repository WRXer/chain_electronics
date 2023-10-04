from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer  # Создайте соответствующий файл serializers.py и определите в нем ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer