from django.urls import path
from .views import ShippingView,CartView

urlpatterns = [
    path('shipping_adress', ShippingView.as_view(), name='shipping_adress'),
    path('cart', CartView.as_view(), name='cart'),
]
