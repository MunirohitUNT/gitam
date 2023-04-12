from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile_number']
