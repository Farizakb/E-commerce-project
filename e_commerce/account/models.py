from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MinValueValidator,MaxValueValidator
# Create your models here.

class User(AbstractUser):
    number = models.CharField(
         max_length=20,validators = [MinLengthValidator(10)], null=True, blank=True
        )
    birthday = models.DateField(
        null=True, blank=True 
        )
    gender = models.CharField(
        max_length = 1,choices=(('1','Man'),('2','Woman')),null=True,blank=True
        )
    