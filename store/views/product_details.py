from store.models import ProductDetail
from store.serializers.product_detail import ProductDetailCreateUpdateSerializer, ProductDetailSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import SAFE_METHODS

class ProductDetailListCreateGenericView(ListCreateAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer

class ProductDetailRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer