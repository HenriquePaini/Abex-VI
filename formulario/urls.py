from django.contrib import admin
# formulario/urls.py
from django.urls import path
from . import views

app_name = 'formularios'

urlpatterns = [
    path('', views.formulario_view, name='formulario'),  # Página principal do formulário
    path('resultado/', views.resultado, name='resultado'),
]



"""
cartão independente, cartão negociavel(nao pode ser o fim), cartão valioso(deve entregar valor. algo)
cartão deve ser estimavel(devo conseguir medir qual vai ser o trabalho dele)
cartão deve ser pequeno(deve ser pequeno o suficiente para ser feito em um dia)
cartão deve ser testavel
"""