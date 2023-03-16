from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,"home.html")

def signup(request):
    return render(request,"signin.html")



def package(request):
    return render(request,"package.html")
def gallary(request):
    return render(request,"gallary.html")
def contactus(request):
    return render(request,"contact.html")
def aboutus(request):
    return render(request,"about.html")
def login(request):
    return render(request,"login.html")
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