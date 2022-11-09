from django.db import models
from blog.models import AbstractModel
# Create your models here.

class Contact(AbstractModel):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    subject = models.CharField(max_length = 250)
    message = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.name}  {self.email}"