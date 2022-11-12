from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm,PasswordResetForm
from django import forms
from django.contrib.auth import get_user_model,authenticate,login
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _



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
        user.is_active = True
        if commit:
            user.save()
        return user
    
    
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Username',
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':'Password',
        }))
    
   
class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password1"].widget = forms.widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = forms.widgets.PasswordInput(attrs={"class":"form-control"})            
    
    
    
    
class CusPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class':'form-control'}),
    )
    
    
    