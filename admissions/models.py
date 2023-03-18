from django.db import models


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
