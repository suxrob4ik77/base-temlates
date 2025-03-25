from django import forms
from .models import *
class SmsForm(forms.ModelForm):
    class Meta:
        model=Sms
        fields='__all__'