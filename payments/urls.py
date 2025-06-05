from django.urls import path
from .views import SolicitarCompraAPIView

urlpatterns = [
    # otras rutas...
    path('compra/', SolicitarCompraAPIView.as_view(), name='solicitar-compra'),
]
