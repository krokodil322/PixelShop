from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('add_product', add_product, name='add_product'),
    path('card_product/<int:product_id>/', card_product, name='card_product'),
    path('change_product/<int:product_id>/', change_product, name='change_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
    path('buy_product/<int:product_fk>', buy_product, name='buy_product'),
]

