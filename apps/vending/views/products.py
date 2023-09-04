from apps.vending.serializers import SlotsSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from apps.vending.models import Slot as SlotModel
from rest_framework.views import APIView
from django.db.models import Max

# Generates a "SELECT MAX..." query


class Products(APIView):
    def get(self, request: Request) -> Response:
        slots = []
        num_rows = list(SlotModel.objects.aggregate(Max("row")).values())[0]

        for i in range(num_rows):
            i = i + 1
            products = SlotModel.objects.all().filter(row=i)
            products_serialized = SlotsSerializer(products, many=True)
            slots.append(products_serialized.data)

        return Response(data=slots)
