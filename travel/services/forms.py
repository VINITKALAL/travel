from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *

class Userform(UserCreationForm):
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = Registration
        fields = ['first_name','last_name','email','password1','password2','photo']


class EditProfileForm(UserChangeForm):
    class Meta:
        model=Registration
        fields=['first_name','last_name','email','photo']

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields=['people_name','city','phone','email','journey_date','total_people','pickup_point','package','registration']
        
        


          

