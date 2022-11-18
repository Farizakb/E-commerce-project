from django.urls import path

from .views import CategoryApiView, ProductApiView,ProductReadUpdateDeleteView,CategoryReadUpdateDeleteView, BasketApiView, BasketRUD


urlpatterns = [
    path('categories/',CategoryApiView.as_view(),name='categories_api'),
    path('products/',ProductApiView.as_view(),name='products_api'),
    path('baskets/',BasketApiView.as_view(),name='baskets_api'),
    path('baskets/<int:pk>/',BasketRUD.as_view(),name='basket_api'),
    path('products/<int:pk>/',ProductReadUpdateDeleteView.as_view(),name='product_api'),
    path('categories/<int:pk>/',CategoryReadUpdateDeleteView.as_view(),name='category_api'),
    
]