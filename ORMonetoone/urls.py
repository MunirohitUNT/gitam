"""ORMonetoone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cellphone import views
from django.contrib.auth.views import LoginView

from cellphone.views import upload_image, upload_success
from cellphone.views import currency_to_words


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('upload/', upload_image, name='upload_image'),
    path('upload/success/', upload_success, name='upload_success'),
    path('qr_code/<str:data>/', views.generate_qr_code, name='generate_qr_code'),
    path('currency-to-words/', currency_to_words, name='currency_to_words'),
    # path('login/', LoginView.as_view(), name='login'),
    path('', views.home, name='home'),
]
