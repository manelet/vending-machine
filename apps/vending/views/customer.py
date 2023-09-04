from rest_framework.response import Response
from rest_framework.request import Request
from apps.vending.models import Customer as CustomerModel
from apps.vending.serializers import CustomerSerializer
import json
from datetime import datetime
from rest_framework.views import APIView


class Customer(APIView):
    def get(self, request: Request) -> Response:
        return Response()

    def post(self, request: Request) -> Response:
        data = json.loads(request.body)

        try:
            customer = CustomerModel.objects.get(name=data["name"])
            customer.last_login = datetime.now()
            customer.save()
        except ObjectDoesNotExist:
            customer = CustomerModel(name=data["name"], credit=0)
            customer.save()

        customer_serializer = CustomerSerializer(customer, many=False)

        return Response(data=customer_serializer.data)
