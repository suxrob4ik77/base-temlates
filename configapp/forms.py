from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *
class SmsForm(forms.ModelForm):
    class Meta:
        model=Sms
        fields='__all__'


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Login',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )