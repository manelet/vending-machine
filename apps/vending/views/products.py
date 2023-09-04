from apps.vending.serializers import SlotSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from apps.vending.models import Slot as SlotModel
from rest_framework.views import APIView


class Products(APIView):
    def get(self, request: Request) -> Response:
        slots = SlotModel.objects.all()
        slots_serializer = SlotSerializer(slots, many=True)
        return Response(data=slots_serializer.data)
