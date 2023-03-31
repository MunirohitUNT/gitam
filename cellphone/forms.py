from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cellphone.models import Image

from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile_number']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['mobile_number']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('caption',)
