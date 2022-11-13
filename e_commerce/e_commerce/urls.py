"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from product.views import CategoriesView

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('categories/', CategoriesView.as_view(), name='categories' ),
    
    path('', include('social_django.urls', namespace='social')),
    path('i18n/', include('django.conf.urls.i18n')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('blogs/', include('blog.urls')),
    path('products/', include('product.urls')),
    path('orders/', include('order.urls')),
    path('account/', include('account.urls')),
    path('api/', include('api.urls')),
    
)