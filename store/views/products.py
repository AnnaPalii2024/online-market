from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from store.models import Product, ProductDetail
from store.serializers.product_detail import ProductDetailSerializer, ProductDetailCreateUpdateSerializer
from store.serializers.products import ProductSerializer, ProductCreateUpdateSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.select_related(
        'category', 'supplier'
    ).all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__name', 'price']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    #authentication_classes = []
    permission_classes = [
        IsAuthenticated
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductDetailListCreateView(ListCreateAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer


class ProductDetailRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer
