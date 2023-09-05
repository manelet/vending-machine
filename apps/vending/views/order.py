from apps.vending.serializers import SlotsSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from apps.vending.models import Slot as SlotModel
from rest_framework.views import APIView
from django.db.models import Max
from apps.vending.models import Customer, Slot
from django.core.exceptions import BadRequest
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import decimal


class Order(APIView):
    def post(self, request: Request) -> Response:
        data = json.loads(request.body)

        try:
            customer = Customer.objects.get(name=data["customer_name"])
            slot = Slot.objects.get(id=data["slot_id"])

            customer.credit = decimal.Decimal(customer.credit) - decimal.Decimal(
                slot.product.price
            )
            slot.quantity = slot.quantity - 1

            customer.save()
            slot.save()
            return JsonResponse({"new_balance": customer.credit})

        except ObjectDoesNotExist:
            raise BadRequest("Customer does not exist.")
