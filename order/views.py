from django.views.generic import DetailView, FormView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from order.forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import request, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


class CartView(LoginRequiredMixin, ListView):
    model = OrderedItem
    template_name = "order/cart.html"
    success_url = "/order/delivery"
    login_url = '/login'


class DeliveryView(LoginRequiredMixin, FormView):
    form_class = DeliveryForm
    template_name = "order/delivery.html"
    success_url = "/order/profile"
    login_url = '/login'

    def form_valid(self, form):
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


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #
    #     user = self.request.user
    #     if user.is_authenticated:
    #         queryset = queryset.filter(user=user)
    #     return queryset

