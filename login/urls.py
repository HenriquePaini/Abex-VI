from django.urls import path
from . import views 

app_name = 'login'  

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('formulario/', views.formulario_view, name='formulario'),
    path('register/', views.register_view, name='register'),  # Adiciona a URL do cadastro
    path('logout/', views.logout_view, name='logout'),
]
