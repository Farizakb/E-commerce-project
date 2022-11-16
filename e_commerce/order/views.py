from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import ShippingForm
from .models import ShippingAddress, Order,Basket
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
    
    
class CartView(TemplateView):
    template_name = 'order/cart.html'
    
    def get(self, request, *args, **kwargs):
        
        context = self.get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            customer = self.request.user.customer
            print(customer)
            order, created = Basket.objects.get_or_create(user = customer, status = False)
            context['items'] = order.basket_item.all()
            
        else:
            context['items'] = []
            
        return self.render_to_response(context)