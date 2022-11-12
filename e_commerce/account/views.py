from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView ,PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView,UpdateView

from .forms import LoginForm, UserRegistration, ChangePasswordForm

# Create your views here.

class LoginRegisterView(TemplateView):
    template_name = "account/login.html"

    
    login_form = LoginForm()
    register_form = UserRegistration()

    def get(self, request, *args, **kwargs):
        print('here_get')
        return self.render_to_response({'login_form': self.login_form, 'register_form': self.register_form})



    def post(self, request, *args, **kwargs):
        if "password1" in request.POST:
            
            form = UserRegistration(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
                if user is not None:
                    login(request, user)
                    return redirect('home')
                    
            else:
                return self.render_to_response({'register_form': form,'login_form': self.login_form})
                
            
            
        if "password" in request.POST:
            print(request.POST)
            form  = LoginForm(data = request.POST)
            if form.is_valid():
                user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('home')
                    
            else:
                return self.render_to_response({'login_form': form,'register_form': self.register_form})
 
 
class ProfileView(TemplateView):
    template_name = 'account/my-account.html'               
            

class PasswordsChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')
    template_name = 'account/change_password.html'




   

    