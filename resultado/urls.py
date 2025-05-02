from django.urls import path
from . import views

app_name = 'resultado'

urlpatterns = [
    path('', views.mostrar_resultado, name='resultado'),  # Página principal do formulário
    path('resultado/', views.mostrar_resultado, name='resultado'),
]
