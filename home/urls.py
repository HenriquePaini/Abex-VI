from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'home'  # Nome do app

urlpatterns = [
    path('', views.home, name='home'),
]
