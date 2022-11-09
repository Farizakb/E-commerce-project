from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView,DetailView
from product.models import Category
# Create your views here.


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    paginate_by = 5
    context_object_name = "blogs"
    
    
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/single-blog.html'
    context_object_name = 'blog'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent_category = None)
        context["blogs"] = Blog.objects.all()
        return context
    