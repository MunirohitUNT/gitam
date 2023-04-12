# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import date


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20)


def __str__(self):
    return f"{self.user.username}'s Profile"


class Image(models.Model):
    caption = models.CharField(max_length=255)
    image_file = models.BinaryField()


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class Cellphone(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()

    def age(self):
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name


class MyFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    path = models.FileField(max_length=255)
    size = models.PositiveIntegerField()


class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name
