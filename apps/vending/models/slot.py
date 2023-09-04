from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator


class Slot(models.Model):
    class Meta:
        db_table = "slot"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    row = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    column = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)]
    )

    objects = models.Manager()
