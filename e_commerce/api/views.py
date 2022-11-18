from multiprocessing import context
from django.http import JsonResponse
from rest_framework.response import Response
from product.models import Product,Category
from order.models import Basket, Basketİtem, Customer
from .serializers import CategorySerailizer ,ProductSerializer, ParentCategorySerailizer,ProductPostSerializer,BasketSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser


class ProductApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = ProductPostSerializer
        return super().get_serializer_class()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    
    
    
class ProductReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_class(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.serializer_class = ProductPostSerializer
        return super().get_serializer_class()
    
    

class CategoryApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerailizer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            self.serializer_class = ParentCategorySerailizer
        return super().get_serializer_class()
    
    
    
class CategoryReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerailizer
    
    def get_serializer_class(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.serializer_class = ParentCategorySerailizer
        return super().get_serializer_class()
    
    
class BasketApiView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user)
        basket = Basket.objects.filter(customer = request.user.customer, status = False) 
        serializer = BasketSerializer(basket,context={'request':request} , many=True )
        return Response(serializer.data, status = 200)
    
    
    def post(self, request, *args, **kwargs):
        print(request.user)
        user = request.data['user']
        action = request.data['action']
        if action == 'remove':
            basket_item_id = request.data['product_id']
            item = Basketİtem.objects.get(id = basket_item_id)
            if item.count > 1 :
                item.count -= 1
                item.save()
            else:
                item.delete()
            
        elif action == 'add':
            
            product_id = request.data['product_id']
        
            customer = Customer.objects.get(user__username = user)
            product = Product.objects.get(id = product_id)
            basket, maked = Basket.objects.get_or_create(customer = customer, status = False)
            print(maked)
            
            basket_item, created= Basketİtem.objects.get_or_create(basket = basket, product = product, count = 1)
            print(created)
            
            if created:
                basket_item.save()
            else:
                basket_item.count += 1
                basket_item.save()
            print("add")
        
        
        return Response("ok", status = 200)
        




class BasketRUD(RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    lookup_field = 'status'
    # def get_serializer_class(self):
    #     if self.request.method in ['PUT','PATCH','DELETE']:
    #         self.serializer_class = ParentCategorySerailizer
    #     return super().get_serializer_class()