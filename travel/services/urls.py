from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    path('', homepage),
    path('homepage/', homepage),
    path('package/', package),
    path('gallary/', gallary),
    path('contactus/', contactus),
    path('aboutus/', aboutus),
    path('login/', login),
    path('fgpass/', fgpass),
    path('signup/', signup),
    path('aa/',aa),
    path('tc/',tc),
    path('pp/',pp),
    path('h/',h1),

]

