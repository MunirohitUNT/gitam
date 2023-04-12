from django.db import models
from django.utils import timezone


# from django_bson import ObjectIdField


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=1000)
    bloodGroup = models.CharField(max_length=10)
    age = models.IntegerField()
    contact = models.CharField(max_length=1000)


# image and date
class Image(models.Model):
    name = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True)


class BmiRecord(models.Model):
    # id = ObjectIdField(primary_key=True)
    id = models.BigAutoField(primary_key=True)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)


def __str__(self):
    return f'Height: {self.height}, Weight: {self.weight}, BMI: {self.bmi}'


class Barcode(models.Model):
    name = models.CharField(max_length=100)
    barcode_image = models.BinaryField(null=True, blank=True)
