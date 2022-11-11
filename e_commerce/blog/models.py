from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify 

# Create your models here.

User = get_user_model()

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    

class Blog(AbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'blog')
    
    title = models.CharField(max_length = 100,db_index =True)
    slug = models.SlugField(max_length = 150,db_index = True, blank = True)
    short_description = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'blog')
    
    
    def __str__(self) -> str:
        return f'{self.author}-->{self.title}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
class BlogComment(AbstractModel):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_comment')
    blogs = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = 'blog_comment')
    
    content = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return f'{self.author}-->{self.content}'