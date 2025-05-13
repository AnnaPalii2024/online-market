from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from store.models import Order, OrderItem
from store.serializers.order import OrderSerializer, OrderCreateUpdateSerializer
from store.serializers.order_item import OrderItemSerializer, OrderItemCreateUpdateSerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer


class OrderDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCreateUpdateSerializer


class OrderItemListCreateView(ListCreateAPIView):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCreateUpdateSerializer


class OrderItemDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return [OrderItemCreateUpdateSerializer]
