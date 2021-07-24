from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_cart, name='view_shopping_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    # path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    # path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]