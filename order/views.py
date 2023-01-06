import datetime
from django.views.generic import DetailView, FormView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from order.forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import request, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

now = datetime.datetime.now()


class CartView(LoginRequiredMixin, ListView):
    model = OrderedItem
    template_name = "cart/cart.html"
    success_url = "/order/delivery"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        u = self.request.user
        order = Order.objects.filter(user=u)
        items = OrderedItem.objects.all()

        context['items'] = items
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
                order = Order.objects.filter(user=u, status=0).get(address='Gagarina street, 55',
                                             date=str(now.year) + '-' + str(now.month) + '-' + str(now.day),
                                             delivery_time_id=1)
                order = Order(**form.cleaned_data)
                cd = form.cleaned_data
                order.address = cd['address']
                order.date = cd['date']
                order.delivery_time_id = cd['delivery_time']
                order.status = 1
                form.save()
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order/profile.html"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        u = self.request.user
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
