from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from order.models import *


class CreateAccountForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'sign_up_form_input', 'placeholder': 'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'sign_up_form_input', 'placeholder': 'Lastname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'sign_up_form_input', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'sign_up_form_input', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'sign_up_form_input', 'placeholder': 'Password',
                                                             'type': 'password'}))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login_form_input', 'placeholder': 'Username'}))
    password = forms.CharField(strip=False, widget=forms.TextInput(attrs={'class': 'login_form_input',
                                                                          'placeholder': 'Password',
                                                                          'autocomplete': 'current-password',
                                                                          'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
