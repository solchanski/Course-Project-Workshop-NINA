import datetime
from django.views.generic.list import ListView
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from store.models import *
from order.models import *

now = datetime.datetime.now()


class CreateBouquetView(ListView):
    model = Item
    template_name = "store/create_bouquet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flowers = Item.objects.filter(type_id=2)
        context['flowers'] = flowers
        return context


@login_required(login_url="/login/")
@require_POST
def get_flower(request, id):
    item = get_object_or_404(Item, id=id)
    u = request.user
    order_existed = Order.objects.filter(user_id=u.id, status=0).exists()
    if order_existed:
        order = Order.objects.filter(user_id=u.id, status=0).get()
        ordered_items = OrderedItem(order_id=order.id, item_id=id, amount=1)
        ordered_items.save()
    else:
        order = Order(user_id=u.id, address='Gagarina street, 55',
                      date=str(now.year) + '-' + str(now.month) + '-' + str(now.day),
                      delivery_time_id=1, status=0)
        order.save()
        ordered_items = OrderedItem(order_id=order.id, item_id=id, amount=1)
        ordered_items.save()
    return render(request, "store/create_bouquet_redirect.html", {"item": item})


@login_required(login_url="/login/")
@require_POST
def get_bouquet(request, id):
    item = get_object_or_404(Item, id=id)
    u = request.user
    order_existed = Order.objects.filter(user_id=u.id, status=0).exists()
    if order_existed:
        order = Order.objects.filter(user_id=u.id, status=0).get()
        ordered_items = OrderedItem(order_id=order.id, item_id=id, amount=1)
        ordered_items.save()
    else:
        order = Order(user_id=u.id, address='Gagarina street, 55',
                      date=str(now.year) + '-' + str(now.month) + '-' + str(now.day),
                      delivery_time_id=1, status=0)
        order.save()
        ordered_items = OrderedItem(order_id=order.id, item_id=id, amount=1)
        ordered_items.save()
    return render(request, "store/show_bouquets_redirect.html", {"item": item})


class ShowBouquetsView(ListView):
    model = Item
    template_name = "store/show_bouquets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bouquets = Item.objects.filter(type_id=1)
        context['bouquets'] = bouquets
        return context
