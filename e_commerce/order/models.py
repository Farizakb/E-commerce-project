from django.db import models
from blog.models import AbstractModel
from django.contrib.auth import get_user_model
from product.models import Product
User = get_user_model()
# Create your models here.


class Country(AbstractModel):
    countries = models.CharField(verbose_name="Country", max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.countries

    


class City(AbstractModel):
    countries = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Country", related_name="City_Country")
    cities = models.CharField(verbose_name="City",max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.cities



class ShippingAddress(AbstractModel):
    user = models.ForeignKey(User, related_name="shipping_address", on_delete=models.CASCADE,)
    company_name = models.CharField(verbose_name="Company name", max_length=255,  null=True, blank=True)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="Shipping_Country")
    cities = models.ForeignKey(City, on_delete=models.CASCADE, related_name="Shipping_City")
    address = models.TextField(verbose_name="Address", null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.user.username} -- > {self.address}'
    
    
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    
    def __str__(self) -> str:
        return self.user.username

  
    
    
class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='basket')
    status = models.BooleanField(default = False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Basket:{self.id}, Status:{self.status}' 
    
    @property
    def get_cart_total(self):
        orderitems = self.basket_item.all()
        total = sum([item.get_total for  item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.basket_item.all()
        total = sum([item.count for item in orderitems])
        return total
    
    
class Basketİtem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket_item')
    basket= models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_item')

    count = models.IntegerField()

    
    def __str__(self) -> str:
        return f'{self.product} -> {self.basket}'
    
    @property
    def get_total(self):
        total = self.product.price * self.count
        return total


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='order')
    total_price = models.DecimalField(decimal_places=2,max_digits=15)