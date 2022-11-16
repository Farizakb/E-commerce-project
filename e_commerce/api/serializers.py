from rest_framework import serializers
from product.models import Product, Category
from order. models import Basket, Customer, Basketİtem


class ParentCategorySerailizer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'parent_category',
        )    
        

class CategorySerailizer(serializers.ModelSerializer):
    parent_category = ParentCategorySerailizer()
    
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent_category',
            'created_at',
            'updated_at',
        )
    
    
    
    
class ProductSerializer(serializers.ModelSerializer):
    categories = ParentCategorySerailizer()
    
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'code',
            'short_description',
            'discounts',
            'categories',
        )
        
        
        
class ProductPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'code',
            'short_description',
            'discounts',
            'categories',
        )
        
        
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields ='__all__'
        
        
class BasketSerializer(serializers.ModelSerializer):
    customer  = CustomerSerializer()

    items = serializers.SerializerMethodField()
    class Meta:
        model = Basket   
        
        fields = (
            'id',
            'customer',
            'status',
            'date_ordered',
            'get_cart_items',
            'get_cart_total',
            'items',
        ) 
    
    def get_items(self,obj):
        serializer = BasketItemSerializer(obj.basket_item.all(),context = self.context,many =True)
        return serializer.data 


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = Basketİtem   
        
        fields = (
            'id',
            'product',
            'basket',
            'get_total',
            'count',
        )                                    
        