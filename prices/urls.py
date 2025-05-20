from django.urls import path
from .views import get_usdt_price

urlpatterns = [
    path('usdt-price/', get_usdt_price, name='usdt-price'),
]
