from django.db import models
from blog.models import AbstractModel
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.
User = get_user_model()

Star_review = (
    (1,"1 Star"),
    (2,"2 Star"),
    (3,"3 Star"),
    (4,"4 Star"),
    (5,"5 Star"),
)
   

class Discount(AbstractModel):
    value = models.IntegerField()
    is_percentage = models.BooleanField(default = True)
    
    def __str__(self) -> str:
        return str(self.value)
    
    
class Category(AbstractModel):
    parent_category = models.ForeignKey('self',on_delete = models.CASCADE, null = True, blank = True, related_name = 'subcategory')
    
    name = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 150,db_index = True,blank = True)
    
    
    def __str__(self) -> str:
        if self.parent_category:
            
            return f'{self.parent_category}-->{self.name}'
        
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.parent_category}-->{self.name}')
        super().save(*args, **kwargs)


class Property(AbstractModel):
    category = models.ManyToManyField(Category,blank = True, related_name = 'property')
    
    title = models.CharField(max_length = 100,db_index = True)
    
    
    def __str__(self) -> str:
        return self.title


class PropertyValue(AbstractModel):
    properties = models.ForeignKey(Property, on_delete = models.CASCADE, related_name = 'property_value')
    
    title = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.title



class Product(AbstractModel):
    categories = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'product')
    discounts = models.ForeignKey(Discount, null = True, blank = True, on_delete = models.SET_NULL, related_name = 'product')
    
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    title = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 150, db_index = True, blank = True)
    code = models.IntegerField()
    short_description = models.CharField(max_length = 255, null = True, blank = True)
    
    
    def __str__(self) -> str:
        return self.title
    
    @property
    def calculated_value(self):
        if self.discounts:
            
            return int(self.price) - (int(self.price) * int(self.discounts.value)) / 100
        
        return self.price
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
class ProductComment(AbstractModel):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'product_comment')
    products = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'product_comment')
    
    content = models.CharField(max_length = 100)
    review = models.CharField(max_length = 1, choices = Star_review)
    
            
    def __str__(self) -> str:
        return f'{self.author}-->{self.products}'


class ProductImages(AbstractModel):
    products = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, blank = True, related_name = 'product_image')
    
    path = models.ImageField(upload_to = 'product_image')
    is_main = models.BooleanField(default = True)
    
    def __str__(self) -> str:
        return f'{self.products}'



class ProductPropertyValue(AbstractModel):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE,related_name = 'product_property')
    property_value = models.ForeignKey(PropertyValue , on_delete = models.CASCADE, related_name = 'product_property')
    
    count = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.product_id} ----> {self.property_value}  ({self.count})'
    
    
    
    
 
    
    