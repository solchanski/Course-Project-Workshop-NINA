import datetime
from django.views.generic import DetailView, FormView, DeleteView, CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from order.forms import *
from django.http import request, HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

now = datetime.datetime.now()


class CartView(LoginRequiredMixin, ListView):
    model = OrderedItem
    template_name = "cart/cart.html"
    success_url = "/order/delivery"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        u = self.request.user
        order = Order.objects.filter(user_id=u.id, status=0).get()
        if OrderedItem.objects.filter(order=order).exists():
            ordered = OrderedItem.objects.filter(order=order)
            context['ordered'] = ordered
            item = OrderedItem.objects.filter(order=order).values_list('item', flat=True)
            total = []
            for i in item:
                price = Item.objects.filter(id=i).values_list('price', flat=True)
                total.append(price[0])
            total_price = sum(total)
            context['total_price'] = total_price
        items = OrderedItem.objects.all()
        context['items'] = items
        context['order'] = order
        return context


class DeliveryView(LoginRequiredMixin, FormView):
    form_class = DeliveryForm
    template_name = "order/delivery.html"
    success_url = "/order/profile"
    login_url = '/login'

    def update(self, form):
        if request.method == 'POST':
            form = DeliveryForm(request.POST)
            if form.is_valid():
                u = self.request.user
                order = Order(**form.cleaned_data)
                order = Order.objects.filter(user=u, status=0).get(address='Gagarina street, 55',
                                             date=str(now.year) + '-' + str(now.month) + '-' + str(now.day),
                                             delivery_time_id=1)
                cd = form.cleaned_data
                order.address = cd['address']
                order.date = cd['date']
                order.delivery_time_id = cd['delivery_time']
                order.status = 1
                form.save(update_fields=['address', 'date', 'delivery_time', 'status'])
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order/profile.html"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        u = self.request.user
        order = Order.objects.filter(user_id=u.id, status=0).get()
        if OrderedItem.objects.filter(order=order).exists():
            item = OrderedItem.objects.filter(order=order).values_list('item', flat=True)
            total = []
            for i in item:
                price = Item.objects.filter(id=i).values_list('price', flat=True)
                total.append(price[0])
            total_price = sum(total)
            context['total_price'] = total_price
        orders = Order.objects.filter(user=u)
        context['orders'] = orders
        return context


class DeleteOrderView(DeleteView):
    model = Order
    template_name = "order/order_delete.html"
    success_url = "/order/profile"


@require_POST
def cart_remove(request, id):
    item = get_object_or_404(OrderedItem, id=id)
    OrderedItem.objects.filter(id=item.id).delete()
    return render(request, "cart/cart_remove.html", {"item": item})
