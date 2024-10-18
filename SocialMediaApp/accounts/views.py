from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from SocialMediaApp.accounts import forms
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    model = User
    form_class = forms.UserRegistrationForm
    template_name = 'common/register-page.html'  # Path to your register template
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    redirect_authenticated_user = True



class UserLogin(LoginView):
    template_name = 'common/login-page.html'
    authentication_form = forms.UserLoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')