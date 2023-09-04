from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=4, decimal_places=2)
