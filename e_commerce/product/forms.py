from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    
    class Meta:
        
        model = ProductComment
        fields = ('content','review',)
        
        widgets = {
            'content': forms.TextInput(attrs={'class':'form-control','row':2}),
            'review': forms.Select(attrs={'class':'form-control '}) 
        }
        
    
    