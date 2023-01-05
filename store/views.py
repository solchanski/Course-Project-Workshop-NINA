from django.views.generic.list import ListView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from store.models import *
from order.models import *


class CreateBouquetView(ListView):
    model = Item
    template_name = "store/create_bouquet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flowers = Item.objects.filter(type_id=2)
        context['flowers'] = flowers
        return context

def get_item(request, item_id):
        item = get_object_or_404(Item, id=item_id)
        u = request.user
        order = Order(request)
        order.add(user_id=u)
        ordered_items = OrderedItem(request)
        ordered_items.add(order_id=order.id,
                          item_id=item_id,
                          amount=1)
        return render(request, "store/create_bouquet.html")


class ShowBouquetsView(ListView):
    model = Item
    template_name = "store/show_bouquets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bouquets = Item.objects.filter(type_id=1)
        context['bouquets'] = bouquets
        return context
