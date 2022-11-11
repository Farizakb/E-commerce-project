from django.contrib import admin
from .models import Blog, BlogComment
# Register your models here.

from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'short_description', )
    list_filter = ('author',)
    search_fields = ('title','author__username','description',)
    

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blogs','author','content',  )
    list_filter = ('blogs','author',)
    search_fields = ('blogs__title','author__username','content',)
    


admin.site.register(BlogComment,BlogCommentAdmin)
admin.site.register(Blog,BlogAdmin)