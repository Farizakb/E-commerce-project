from django.contrib import admin
from .models import Blog, BlogComment
# Register your models here.



admin.site.register(BlogComment)
admin.site.register(Blog)