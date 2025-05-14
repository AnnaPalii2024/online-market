from rest_framework import viewsets

from store.models import Address
from store.serializers.address import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
