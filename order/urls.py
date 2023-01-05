from django.urls import path
from order import views


urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('delivery/', views.DeliveryView.as_view(), name='delivery'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>', views.DeleteOrderView.as_view(), name='delete_order'),
]
