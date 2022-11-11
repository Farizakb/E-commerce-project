from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistration(UserCreationForm):
    
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password1',"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password2',"autocomplete": "new-password"}),
        strip=False,
    )
    
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }
        
    def save(self, commit=True):
        user = super().save(commit=False) 
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user