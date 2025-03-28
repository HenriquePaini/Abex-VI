from django.shortcuts import render

# Create your views here.

def home(request):  #Função que recebe uma request e retorna uma response
    print('home')
    return render(request, 'home/home.html')