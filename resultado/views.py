# Em: resultado/views.py

from django.shortcuts import render
from django.http import HttpRequest

def mostrar_resultado(request: HttpRequest):
    # Pega os dados da sessão (ainda com as chaves em inglês que definimos na view do formulário)
    prediction_value = request.session.get('prediction', None)
    probability_value = request.session.get('probability', None)
    
    # Limpa os dados da sessão para não ficarem "presos" lá em futuras visitas
    if 'prediction' in request.session:
        del request.session['prediction']
    if 'probability' in request.session:
        del request.session['probability']
    
    # --- A MUDANÇA É AQUI ---
    # Cria o dicionário 'context' com os nomes em PORTUGUÊS, que é o que o seu template espera.
    context = {
        'predicao': prediction_value,       # Enviando como 'predicao'
        'probabilidade': probability_value, # Enviando como 'probabilidade'
    }
    
    # Renderiza o template, agora com as variáveis corretas
    return render(request, 'resultado/resultado.html', context)