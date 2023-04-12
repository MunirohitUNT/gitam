from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from .models import UserProfile, Image
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from cellphone.forms import ImageForm
import qrcode
import io
from num2words import num2words
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from cellphone.models import Cellphone
from .forms import CellphoneForm
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import ProductForm
from .models import MyFile
from django.core.files.base import ContentFile
from .forms import FileUploadForm
from django.http import HttpResponseRedirect
import pytz
from django.shortcuts import render
from .forms import CountryForm


# Create your views here.

def home(request):
    return HttpResponse(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            mobile_number = form.cleaned_data.get('mobile_number')
            profile = UserProfile(user=user, mobile_number=mobile_number)
            profile.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # print(form)
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'form': form})


'''
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.data = request.FILES['data'].read()
            image.save()
            return render(request, 'upload_success.html')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})
'''


def upload_image(request):
    if request.method == 'POST':
        image = Image()
        if 'data' in request.FILES:
            image.data = request.FILES['data'].read()
        image.save()
        return redirect('profile')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})


def upload_success(request):
    message = "Image uploaded successfully."
    return render(request, 'upload_success.html', {'message': message})


def generate_qr_code(request, data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, 'PNG')
    image_binary = buffer.getvalue()
    response = HttpResponse(image_binary, content_type='image/png')
    # response = HttpResponse(content_type='image/png')
    # img.save(response, 'PNG')
    return response


def currency_to_words(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        amount_words = num2words(amount)
        return render(request, 'currency_to_words.html', {'amount': amount, 'amount_words': amount_words})
    else:
        return render(request, 'currency_to_words.html')


class CellphoneCreateView(CreateView):
    model = Cellphone
    form_class = CellphoneForm
    success_url = reverse_lazy('cellphone_list')
    template_name = 'dobcellphone_form.html'

    def form_valid(self, form):
        self.object = form.save()
        context = self.get_context_data(object=self.object)
        context['age'] = self.object.age()
        return self.render_to_response(context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


'''
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            file_obj = File(name=file.name, path=file.path, size=file.size)
            file_obj.save()
            return HttpResponseRedirect('/files/')
    else:
        form = FileUploadForm()
    return render(request, 'uploadfile.html', {'form': form})
'''


def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        file_contents = uploaded_file.read()
        file_obj = MyFile(name=uploaded_file.name, size=len(file_contents))
        file_obj.path.save(uploaded_file.name, ContentFile(file_contents))
        file_obj.save()
        return render(request, 'upload_successfull.html', {'file_id': str(file_obj.id)})
    else:
        return render(request, 'upload_form.html')


def file_list(request):
    files = MyFile.objects.all()
    return render(request, 'file_list.html', {'files': files})


def get_timezone_for_country(country):
    timezones = pytz.country_timezones.get(country, [])
    if timezones:
        return pytz.timezone(timezones[0])


def timezone_view(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country']
            timezone = get_timezone_for_country(country.code)
            return render(request, 'timezone.html', {'timezone': timezone})
    else:
        form = CountryForm()
    return render(request, 'timezone_form.html', {'form': form})
