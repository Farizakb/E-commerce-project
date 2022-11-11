from django.contrib import admin
from .models import Product, ProductComment, Category, Property, PropertyValue, Discount, ProductImages, ProductPropertyValue 
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent_category','name',)
    list_filter = ('name','parent_category')
    search_fields = ('name',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('value','is_percentage')
    list_filter = ('is_percentage',)
    search_fields = ('name',)
    list_editable = ('is_percentage',)


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('products','path','is_main',)
    list_filter = ('products','is_main',)
    search_fields = ('products__title',)
    list_editable = ('is_main',)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('category',)
    search_fields = ('category__name','title')


class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ('title','properties',)
    list_filter = ('properties',)
    search_fields = ('properties__title','title')


class ProductPropertyValueAdmin(admin.ModelAdmin):
    list_display = ('product_id','property_value', 'count')
    list_filter = ('product_id','property_value','count')
    search_fields = ('product_id__title','property_value__title')
    list_editable = ('count',)


class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('author','products', 'content','review')
    list_filter = ('author','products','review')
    search_fields = ('content',)
    list_editable = ('review',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('categories','title','price', 'discounts','code',)
    list_filter = ('categories','discounts',)
    search_fields = ('title','short_description')
    list_editable = ('discounts',)



admin.site.register(Product,ProductAdmin)
admin.site.register(ProductComment,ProductCommentAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(PropertyValue,PropertyValueAdmin)
admin.site.register(Discount,DiscountAdmin)
admin.site.register(ProductPropertyValue,ProductPropertyValueAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)