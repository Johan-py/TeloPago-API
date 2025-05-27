from django.urls import path
from .views import PreregistroCreateView

urlpatterns = [
    path('register/', PreregistroCreateView.as_view(), name='preregistro-create'),
]
