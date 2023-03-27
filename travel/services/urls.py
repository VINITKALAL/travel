from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout_then_login

urlpatterns = [

    path('signin/', UserRegistration.as_view(), name='signup'),
    path('', homepage),
    path('homepage/', homepage,name="homepage"),
    path('home1/', home1,name="home1"),
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


    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='changepassword.html',
            success_url = '/home1/'
        ),
        name='change_password'),


    path(
        'login/',
        auth_views.LoginView.as_view(
        template_name='register.html',
        success_url= '/home1/',
        ),
        name='login'),

    path('logout_then_login/',logout_then_login,name='logout_then_login')


]

