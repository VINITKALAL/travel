from django.shortcuts import render
from django.views.generic import CreateView,FormView,View,UpdateView,DetailView,DeleteView
from .models import Registration,Package
from django.http import HttpResponse
from .forms import *
from django.views.generic.base import TemplateView

class UserRegistration(CreateView,FormView):
    model=Registration
    form_class=Userform
    template_name = 'signin.html'
    success_url= '/login/'

# class Homepage(TemplateView):
#     model = Package
#     template_name='home1.html'
#     context_object_name = 'package'
    
    



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
def myprofile(request):
    return render(request,"myprofile.html")