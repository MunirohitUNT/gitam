# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=20)


def __str__(self):
    return f"{self.user.username}'s Profile"


class Image(models.Model):
    caption = models.CharField(max_length=255)
    image_file = models.BinaryField()
