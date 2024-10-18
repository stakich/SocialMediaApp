from django import forms
from SocialMediaApp.accounts.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']