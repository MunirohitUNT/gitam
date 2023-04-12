from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cellphone.models import Image, Country
from cellphone.models import Cellphone
from .models import UserProfile
from cellphone.models import Product


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


class CellphoneForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Cellphone
        fields = ['name', 'dob']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['item_name', 'price']
        widgets = {
            'price': forms.TextInput(attrs={'type': 'number', 'step': '0.01'}),
        }


class FileUploadForm(forms.Form):
    file = forms.FileField()


class CountryForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label=None)
