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
        print(form)
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
