from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    credit = serializers.FloatField()
    created_at = serializers.DateTimeField()
    last_login = serializers.DateTimeField()
