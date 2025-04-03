from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import get_messages  # Para limpar mensagens antigas
from .forms import CustomUserCreationForm
from .models import CustomUser

#  VIEW DE LOGIN
def login_view(request):
    messages.get_messages(request).used = True  # Limpa as mensagens antigas

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home:home')
        else:
            messages.error(request, "Email ou senha inválidos!")

    return render(request, 'login/login.html')


#  VIEW DE CADASTRO
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")  
            return redirect("login:login")  # Redireciona para a tela de login
        else:
            messages.error(request, "Erro ao cadastrar. Verifique os dados!")

    else:
        form = CustomUserCreationForm()

    return render(request, "cadastro/cadastro.html", {"form": form})


#  VIEW DE LOGOUT
def logout_view(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect("home:home")


#  OUTRAS VIEWS (Se precisar delas)
def cadastro_view(request):
    return render(request, "cadastro/cadastro.html")

def formulario_view(request):
    return render(request, "formulario/formulario.html")
