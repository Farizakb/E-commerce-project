from django.shortcuts import render
from .models import Product, ProductPropertyValue, Property,Category, PropertyValue
from django.views.generic import ListView,DetailView
# Create your views here.


class ProductView(ListView):
    model = Product
    template_name = 'product/product-list.html'
    paginate_by = 4
    context_object_name = "products"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query_q = self.request.GET.get('q')
        print(query_q)
        if query_q:
            quey_q_set = query_q.split(' ')
            queryset = queryset.filter(title__icontains = quey_q_set[0])
            queryset = queryset.filter(title__icontains = quey_q_set[1])
        return queryset.order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent_category = None)
        context["discount_products"] = Product.objects.filter(discounts__value__gte = 20)
        context["properties"] = Property.objects.all()
        return context
    
    
    
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/single-product.html'
    context_object_name = 'product'
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent_category = None)
        values = PropertyValue.objects.filter(product_property__product_id = self.object)  #order_by('pub_date').distinct('pub_date')
        context["values"] = values
        context["properties"] = values.order_by('properties').distinct('properties')
        context["products"] = Product.objects.all().order_by('-created_at')[:4]
        
        return context
    
    
    
class CategoriesView(ListView):
    ...