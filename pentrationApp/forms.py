from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-floating mb-3"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control form-floating mb-3"})
    )