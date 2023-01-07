from django.contrib import admin

from order.models import *


class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ["order", "item"]
    list_filter = ["order"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "date", "delivery_time", "status"]
    list_filter = ["status", "user"]


admin.site.register(Time)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem, OrderedItemAdmin)
