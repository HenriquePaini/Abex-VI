from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'formulario'  # Nome do app

urlpatterns = [
    path('formulario/', views.formulario, name='formulario'),
]