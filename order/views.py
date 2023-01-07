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
        if Order.objects.filter(user_id=u.id, status=0).exists():
            order = Order.objects.filter(user_id=u.id, status=0).get()
            context['order'] = order
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
        return context


def delivery_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = DeliveryForm(request.POST, instance=order)
        if form.is_valid():
            order.user = request.user
            order.status = Order.objects.filter(user_id=request.user.id, status=0).update(status=1)
            order.save()
            return redirect('profile')
    else:
        form = DeliveryForm(instance=order)
    return render(request, 'order/delivery.html', {'form': form})


class ProfileView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order/profile.html"
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        u = self.request.user
        # order = Order.objects.filter(user_id=u.id, status=1)
        # for o in order:
        #     if OrderedItem.objects.filter(order=o).exists():
        #         item = OrderedItem.objects.filter(order=o).values_list('item', flat=True)
        #         total = []
        #         for i in item:
        #             price = Item.objects.filter(id=i).values_list('price', flat=True)
        #             total.append(price[0])
        # total_price = sum(total)
        # context['total_price'] = total_price
        orders = Order.objects.filter(user=u, status=1)
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
