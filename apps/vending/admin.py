from django.contrib import admin
from apps.vending.models import Product
from apps.vending.models import Customer
from apps.vending.models import Slot


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "credit", "created_at", "last_login"]


class SlotAdmin(admin.ModelAdmin):
    list_display = ["product", "row", "column", "quantity"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Slot, SlotAdmin)
