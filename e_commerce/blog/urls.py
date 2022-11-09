from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogView.as_view(), name='blogs'),
    path('<slug:slug>/',views.BlogDetailView.as_view(), name='blog_detail'),
]
