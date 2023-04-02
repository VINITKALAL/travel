from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('', home1,name='homepage1'),
    path('signup/', UserRegistration.as_view(), name='signup'),
    path('homepage/', homepage,name='homepage'),
    # path('homepage/', homepage,name="homepage"),
    # path('home1/', home1,name="home1"),
    path('package/', package),
    path('gallary/', gallary),
    path('contactus/', contactus),
    path('aboutus/', aboutus),
    # path('login/', login),
    path('fgpass/', fgpass),
    path('aa/',aa),
    path('tc/',tc),
    path('pp/',pp),
    path('h/',h1),
    path('pay/',payment),
    path('con/',confirm),
    path('myprofile/',myprofile),

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change.html',
            success_url = '/home1/'
        ),
        name='change_password'),


    path(
        'login/',
        auth_views.LoginView.as_view(
        template_name='login.html',
        success_url= '/homepage/',
        ),
        name='login'),

    path('logout_then_login/',logout_then_login,name='logout_then_login')


]

