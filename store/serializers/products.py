from rest_framework import serializers
from store.models import Product
from store.serializers.supplier import SupplierSerializer
from store.serializers.categoris import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    
