from apps.vending.serializers import SlotsSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from apps.vending.models import Slot as SlotModel
from rest_framework.views import APIView
from django.db.models import Max
from apps.vending.models import Customer
from django.core.exceptions import BadRequest
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


class Wallet(APIView):
    def put(self, request: Request) -> Response:
        data = json.loads(request.body)

        try:
            customer = Customer.objects.get(name=data["customer_name"])
            customer.credit = data["new_balance"]
            customer.save()
            return HttpResponse(status=204)

        except ObjectDoesNotExist:
            raise BadRequest("Customer does not exist.")
