from rest_framework import serializers
from . import models


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeliveryAddress
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasketItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'
