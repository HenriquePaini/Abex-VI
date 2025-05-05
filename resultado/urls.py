from django.urls import path
from . import views

app_name = 'resultado'

urlpatterns = [
    path('resultado/', views.mostrar_resultado, name='resultado'),
]



