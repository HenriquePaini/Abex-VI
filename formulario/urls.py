
from django.urls import path
from . import views

app_name = 'formulario'

urlpatterns = [
    #URL para MOSTRAR o formulário para o usuário
    path('', views.formulario_view, name='formulario_view'),
    
    #URL para PROCESSAR os dados enviados pelo formulário
    path('predict/', views.processar_predicao, name='processar_predicao'),

]

"""
cartão independente, cartão negociavel(nao pode ser o fim), cartão valioso(deve entregar valor. algo)
cartão deve ser estimavel(devo conseguir medir qual vai ser o trabalho dele)
cartão deve ser pequeno(deve ser pequeno o suficiente para ser feito em um dia)
cartão deve ser testavel
"""