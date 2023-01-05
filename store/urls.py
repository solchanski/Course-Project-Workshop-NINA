from django.urls import path
from store import views


urlpatterns = [
    path('create_bouquet/', views.CreateBouquetView.as_view(), name="create_bouquet"),
    path('create_bouquet/<int:id>', views.get_item, name="get_item"),
    path('show_bouquets/', views.ShowBouquetsView.as_view(), name='show_bouquets'),
    # path('create_bouquet/<int:id>', views.get_flower, name="flower"),
    # path('show_bouquets/<int:id>', views.get_bouquet, name="bouquet"),
]