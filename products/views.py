from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """
        Сохраняем продукт в базе данных с автором, который является текущим пользователем, отправившим запрос.
        """
        serializer.save(author=self.request.user)