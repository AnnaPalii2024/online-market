from rest_framework import serializers
from store.models import OrderItem
from store.serializers.products import ProductSerializer
from store.serializers.order import OrderSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate_quantity(self, value):
        if value > 1000:
            raise serializers.ValidationError(
                'Количество товара должно быть не больше тысячи.'
            )
        return value
