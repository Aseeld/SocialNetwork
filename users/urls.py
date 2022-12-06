from django import views
from django.urls import include,path
from users.views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views


from .forms import UserPasswordResetForm,UserPasswordChangeForm


urlpatterns = [
    path("", LoginView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    
    path('password_reset/', 
    auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',    
    form_class=UserPasswordResetForm),
    name='password_reset'),

    path('password_change/', 
    auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html',    
    form_class=UserPasswordChangeForm),
    name='password_change'),

    ]

