import datetime

from django.views.generic import DetailView, FormView, DeleteView, CreateView
from django.urls import reverse
from django.contrib.auth.views import LoginView
from shop.forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password


class CreateAccountView(FormView):
    form_class = CreateAccountForm
    template_name = "registration/sign_up.html"
    success_url = "/login"

    def form_valid(self, form):
        user = User(**form.cleaned_data)
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = LoginForm
    template_name: "registration/login.html"

    def get_success_url(self, **kwargs):
        u = self.request.user
        if u.is_superuser:
            return reverse('admin:index')
        elif u.is_anonymous:
            return reverse('sing_up')
        else:
            return reverse('index')


def index(request):
    return render(request, "index.html")
