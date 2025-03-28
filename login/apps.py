from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'login'

class CadastroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cadastro'
