from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    
    class Meta:
        model = ShippingAddress
        fields = ('company_name','countries','cities','address')
        widgets = {
            'company_name': forms.TextInput(attrs={'class':'form-control'}),
            'cities':forms.Select(attrs={'class':'form-control '}),
            'contries': forms.Select(attrs={'class':'form-control '}),
            'adress': forms.Textarea(attrs={'class':'form-control'}),
        }
        