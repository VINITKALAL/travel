from django.db import models
from django.contrib.auth.models import AbstractUser

class Registration(AbstractUser):
    email = models.EmailField(max_length=254,unique=True)
    photo = models.ImageField(upload_to="profile/",null=True,blank=True)

class Package(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="package_profile/")
    description = models.CharField(max_length=500)
    Price = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.name