from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CusPasswordResetForm

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('login', views.LoginRegisterView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('change_password', views.PasswordsChangeView.as_view(), name='change_password'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "account/reset_password.html",form_class = CusPasswordResetForm), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "account/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "account/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "account/password_reset_done.html"), name ='password_reset_complete')
    
    
]
