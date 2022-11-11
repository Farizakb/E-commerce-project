from django.urls import path
from .views import ShippingView

urlpatterns = [
    path('shipping_adress', ShippingView.as_view(), name='shipping_adress')
]
