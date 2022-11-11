from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ShippingForm
from .models import ShippingAddress
# Create your views here.
class ShippingView(CreateView):
    form_class = ShippingForm
    template_name = 'order/checkout.html'
    success_url = reverse_lazy('shipping_adress')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adress"] = ShippingAddress.objects.filter(user = self.request.user)
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)