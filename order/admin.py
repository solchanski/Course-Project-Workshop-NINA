from django.contrib import admin

from order.models import *

#
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ["amount", "currency", "user"]
#     list_filter = ["currency"]


admin.site.register(Time)
admin.site.register(Order)
admin.site.register(OrderedItem)
