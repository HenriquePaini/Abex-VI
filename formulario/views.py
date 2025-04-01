from django.shortcuts import render

# Create your views here.
# HTTP Request <-> HTTP Response
# MVT (MVC): Model View controller

def formulario(request):  #Função que recebe uma request e retorna uma response
    print('formulario')
    return render(request, 'formulario/formulario.html')

def resultado(request):  #Função que recebe uma request e retorna uma response
    print('resultado')
    return render(request, 'resultado/resultado.html')