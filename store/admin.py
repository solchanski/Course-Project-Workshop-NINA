from django.contrib import admin

from store.models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "price", "type"]
    list_filter = ["type"]


admin.site.register(Type)
admin.site.register(Item, ItemAdmin)
