from django import forms
from admissions.models import Student
from .models import Image
from admissions.models import Barcode


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class VendorForm(forms.Form):
    name = forms.CharField()
    bloodgroup = forms.CharField()
    age = forms.IntegerField()
    contact = forms.CharField()


# image and date
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('name', 'image_file',)


class BarcodeForm(forms.ModelForm):
    class Meta:
        model = Barcode
        fields = ('name',)
