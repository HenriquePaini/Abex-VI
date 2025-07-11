"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),  # Inclui as URLs do app 'home'
    path('login/', include(('login.urls', 'login'), namespace='glycosense')),  # Define o namespace corretamente
    path('formulario/', include(('formulario.urls', 'formulario'), namespace='formulario')),  # Inclui as URLs do app 'formulario'
    path('resultado/', include(('resultado.urls', 'resultado'), namespace='resultado')), # Inclui as URLs do app 'resultado'
    path('admin/', admin.site.urls),

]


