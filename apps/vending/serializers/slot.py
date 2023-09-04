from rest_framework import serializers
from apps.vending.serializers import ProductSerializer


class SlotsSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    product = ProductSerializer()
    # coordinates = serializers.SerializerMethodField()

    # def get_coordinates(self, instance) -> list[int, int]:
    # return [instance.column, instance.row]
