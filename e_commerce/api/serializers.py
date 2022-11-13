from rest_framework import serializers
from product.models import Product, Category


class ParentCategorySerailizer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Category
        fields = (
            'name',
            'created_at',
            'updated_at',
            'parent_category',
        )    
        


class CategorySerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'name',
            'parent_category',
            'created_at',
            'updated_at',
        )
        
    # def get_parent_category(self,obj):
    #     serializer = ParentCategorySerailizer(obj.self.all(),context = self.context,many =True)
    #     return serializer.data