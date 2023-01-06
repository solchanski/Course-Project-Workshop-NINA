from django.urls import path
from store import views


urlpatterns = [
    path('create_bouquet/', views.CreateBouquetView.as_view(), name="create_bouquet"),
    path('create_bouquet/<int:id>', views.get_flower, name="get_flower"),
    path('show_bouquets/', views.ShowBouquetsView.as_view(), name='show_bouquets'),
    path('show_bouquets/<int:id>', views.get_bouquet, name="get_bouquet"),
]