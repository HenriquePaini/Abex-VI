from django.urls import path
from . import views  # Importa as views do app 'resultado'

# Define o namespace do app. Essencial para o 'resultado:mostrar_resultado' funcionar.
app_name = 'resultado'

urlpatterns = [
    # AQUI ESTÁ A DEFINIÇÃO DA ROTA QUE FALTAVA:
    # Caminho: '' (vazio, pois o prefixo '/resultado/' já está no urls.py do projeto)
    # View: views.mostrar_resultado
    # Nome: 'mostrar_resultado' (a identidade que o Django estava procurando)
    path('', views.mostrar_resultado, name='mostrar_resultado'),
]