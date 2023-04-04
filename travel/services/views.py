from django.shortcuts import render
from django.views.generic import CreateView,FormView,View,UpdateView,DetailView,DeleteView,View
from .models import Registration,Package
from django.http import HttpResponse
from .forms import *
from django.views.generic.base import TemplateView

class UserRegistration(CreateView,FormView):
    model=Registration
    form_class=Userform
    template_name = 'signin.html'
    success_url= '/login/'


class Editprofile(UpdateView): 
    model = Registration
    template_name = 'changeprofile.html'
    form_class=  EditProfileForm
    success_url='/homepage/'  
    

# class Booking(View):
#     def get(self, request):
#         packages = Package.objects.all()
#         return render(request,"book.html",{'packages':packages})

class Booking(CreateView,FormView):
    model=Booking
    form_class=Bookingform
    template_name = 'book.html'
    success_url= '/homepage/'

def add_show(request):
    return render(request,'home.html')

def signup(request):
    return render(request,"signin.html")

def homepage(request):
    packages = Package.objects.all()
    return render(request,"home1.html",{'packages':packages})

def home1(request):
    return render(request,"home.html")

def package(request):
    packages = Package.objects.all()
    return render(request,"package1.html",{'packages':packages})

def package1(request):
    packages = Package.objects.all()
    return render(request,"package.html",{'packages':packages})

def gallary(request):
    return render(request,"gallary.html")
def contactus(request):
    return render(request,"contact.html")
def aboutus(request):
    return render(request,"about.html")
# def login(request):
#     return render(request,"login.html")
def fgpass(request):
    return render(request,"fgpass.html")

def aa(request):
    return render(request,"book.html")
def tc(request):
    return render(request,"t&c.html")
def h1(request):
    return render(request,"home1.html")
def pp(request):
    return render(request,"pp.html")
def payment(request):
    return render(request,"payment.html")
def confirm(request):
    return render(request,"confirmdetails.html")
def changeprofile(request):
    return render(request,"change.html")
def p1(request):
    return render(request,"package1.html")
def g1(request):
    return render(request,"gallary1.html")
def c1(request):
    return render(request,"contact1.html")
def rv(request):
    return render(request,"review.html")
def profile(request):
    return render(request,"myprofile.html")
def chprofile(request):
    return render(request,"changeprofile.html")
