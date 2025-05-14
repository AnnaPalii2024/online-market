from rest_framework import viewsets

from store.models import Category
from store.serializers.categoris import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
