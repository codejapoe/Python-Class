from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('signup', views.signup, name='Sign Up'),
    path('signin', views.signin, name='Sign In'),
    path('register', views.register, name='Register'),
    path('login', views.login, name='Login'),
]
