from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'core/index.html') 



class ContactView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('home')
    template_name = 'core/contact.html'

    
    
    