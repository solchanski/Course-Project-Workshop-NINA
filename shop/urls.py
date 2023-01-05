"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from shop import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('sign_up/', views.CreateAccountView.as_view(), name="sign_up"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', authViews.LogoutView.as_view(next_page='/'), name="logout"),
    path('store/', include("store.urls")),
    path('order/', include("order.urls")),
]



