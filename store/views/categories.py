from rest_framework.viewsets import ModelViewSet
from store.models import Category
from store.serializers.categoris import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer