from rest_framework.viewsets import ModelViewSet
from store.models import Product
from store.serializers.products import *
from rest_framework.permissions import SAFE_METHODS


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ProductSerializer
        return ProductCreateUpdateSerializer