from rest_framework import serializers
from apps.vending.serializers import ProductSerializer


class SlotsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    quantity = serializers.IntegerField()
    product = ProductSerializer()
