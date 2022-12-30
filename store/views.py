from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import *


class CreateBouquetView(ListView):
    model = Item
    template_name = "store/create_bouquet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flowers = Item.objects.filter(type_id=2)
        context['flowers'] = flowers
        return context


class ShowBouquetsView(ListView):
    model = Item
    template_name = "store/show_bouquets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bouquets = Item.objects.filter(type_id=1)
        context['bouquets'] = bouquets
        return context
