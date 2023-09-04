# Generated by Django 4.2.2 on 2023-09-02 16:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("vending", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VendingMachineSlot",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ]
                    ),
                ),
                (
                    "row",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                (
                    "column",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vending.product",
                    ),
                ),
            ],
            options={
                "db_table": "vending_machine_slot",
            },
        ),
    ]
