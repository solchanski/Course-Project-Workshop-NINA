from django.urls import path
from order import views


urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('delivery/<int:pk>/edit', views.delivery_edit, name='delivery'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>', views.DeleteOrderView.as_view(), name='delete_order'),
    path('remove/<int:id>', views.cart_remove, name='cart_remove'),
]
