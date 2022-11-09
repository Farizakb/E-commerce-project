from django.contrib import admin
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email","number","gender","birthday")}),
        (_("Permissions"),{
                "fields": ("is_active","is_staff","is_superuser","groups","user_permissions",),
                },),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
      

admin.site.register(User,UserAdmin)