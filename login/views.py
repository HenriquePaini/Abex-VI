from django.shortcuts import render

# Create your views here.
# HTTP Request <-> HTTP Response
# MVT (MVC): Model View controller


def login(request):  #Função que recebe uma request e retorna uma response
    print('login')
    return render(request, 'login/login.html') # Com o parametro contexto, posso adicionar dados extras para serem renderizados no template
# O render é uma função que recebe uma request e um template e retorna uma response

def cadastro(request):  #Função que recebe uma request e retorna uma response
    print('cadastro')
    return render(request, 'cadastro/cadastro.html')

def formulario(request):  #Função que recebe uma request e retorna uma response
    print('formulario')
    return render(request, 'formulario/formulario.html')