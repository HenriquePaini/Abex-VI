from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'glycosense'  # Nome do app

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('formulario/', views.formulario, name='formulario'),
]
