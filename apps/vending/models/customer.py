from django.db import models
from uuid import uuid4


class Customer(models.Model):
    class Meta:
        db_table = "customer"

    name = models.CharField(primary_key=True, editable=False, max_length=100)
    credit = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)

    objects = models.Manager()
