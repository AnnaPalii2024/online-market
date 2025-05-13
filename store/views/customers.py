from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from store.models import Customer
from store.serializers.customer import CustomerSerializer, CustomerCreateUpdateSerializer


class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last__name', 'date_joined']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer


class CustomerDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer
