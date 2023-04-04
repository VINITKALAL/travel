from django.db import models
from django.contrib.auth.models import AbstractUser

class Registration(AbstractUser):
    username = None
    first_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254,unique=True)
    photo = models.ImageField(upload_to="profile/",null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [first_name]

class Package(models.Model):
    name = models.CharField(max_length=250)
    duration = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="package_profile/")
    description = models.CharField(max_length=500)
    Price = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    ROLE = (
    ('ahmedabad', 'AHMEDABAD'),
    ('surat', 'SURAT'),
    ('rajkot', 'RAJKOT'),
    ('baroda', 'BARODA'),
    ('bhavnagar', 'BHAVNAGAR'),
    ('bhuj', 'BHUJ'),
    )
    people_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    journey_date = models.DateField()
    total_people = models.IntegerField()
    pickup_point = models.CharField(max_length=50, choices=ROLE)
    package=models.ForeignKey(Package,on_delete=models.CASCADE,related_name='packages')
    registration = models.ForeignKey(Registration,on_delete=models.CASCADE,related_name='registrations')

    def __str__(self):
        return self.people_name
        


