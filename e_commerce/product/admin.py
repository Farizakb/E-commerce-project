from django.contrib import admin
from .models import Product, ProductComment, Category, Property, PropertyValue, Discount, ProductImages, ProductPropertyValue 
# Register your models here.



admin.site.register(Product)
admin.site.register(ProductComment)
admin.site.register(Category)
admin.site.register(Property)
admin.site.register(PropertyValue)
admin.site.register(Discount)
admin.site.register(ProductPropertyValue)
admin.site.register(ProductImages)