from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from order.models import *


class DeliveryForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Date',
                                                         'type': 'date', 'min': '2023-01-01'}))
    delivery_time = forms.ModelChoiceField(empty_label='Delivery time', queryset=Time.objects.all(),
                                           widget=forms.Select(attrs={'class': 'input2'}))

    class Meta:
        model = Order
        fields = ('address', 'date', 'delivery_time')
