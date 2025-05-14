import re

from rest_framework import serializers
from store.models import Customer
from store.serializers.address import AddressSerializer


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['date_joined', 'deleted', 'deleted_at']
        exclude = ['email', 'phone_number']


class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    def validate_phone_number(self, value):
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError(
                'Номер телефона должен содержать от 10 до 15 цифр.'
            )
