from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import ProductComment

# @receiver(pre_save, sender = ProductComment)
# def my_callback(sender, instance, *args, **kwargs):
#     instance.author = slugify(instance.title)