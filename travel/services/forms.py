from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Registration

class Userform(UserCreationForm):
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = Registration
        fields = ['first_name','last_name','email','password1','password2','photo']
        


          

