from django.forms import ModelForm
from .models import ProductComment

class ProductCommentForm(ModelForm):
    
    class Meta:
        
        model = ProductComment