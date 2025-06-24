# Arquivo: formulario/views.py

from django.shortcuts import render, redirect
from django.http import HttpRequest
import requests # Biblioteca para fazer chamadas HTTP

# View para exibir a página do formulário
def formulario_view(request: HttpRequest):
    return render(request, 'formulario/formulario.html')

# View para processar o formulário e chamar a API
def processar_predicao(request: HttpRequest):
    if request.method == 'POST':
        # 1. Coletar os dados do formulário
        try:
            features = [
                float(request.POST.get('pregnancies')),
                float(request.POST.get('glucose')),
                float(request.POST.get('blood_pressure')),
                float(request.POST.get('skin_thickness')),
                float(request.POST.get('insulin')),
                float(request.POST.get('bmi')),
                float(request.POST.get('diabetes_pedigree')),
                float(request.POST.get('age')),
            ]
        except (ValueError, TypeError):
            # Retorna um erro se os dados não forem numéricos
            return render(request, 'formulario/formulario.html', {'error': 'Erro: Todos os campos devem ser preenchidos com valores numéricos válidos.'})

        # 2. Chamar a API Flask para obter a predição
        API_URL = 'http://127.0.0.1:5000/predict'
        payload = {'features': features}

        try:
            # Faz a requisição POST para a API
            response = requests.post(API_URL, json=payload, timeout=5) # Timeout de 5 segundos
            response.raise_for_status()  # Lança um erro para respostas 4xx/5xx

            # Pega o resultado JSON da API
            api_result = response.json()
            
            # Salva o resultado na sessão para usar na página de resultado
            request.session['prediction'] = api_result.get('prediction')
            request.session['probability'] = api_result.get('probability')

        except requests.exceptions.Timeout:
            error_message = "Erro: A API de predição demorou muito para responder (Timeout)."
            return render(request, 'formulario/formulario.html', {'error': error_message})
        except requests.exceptions.RequestException:
            error_message = "Erro: Não foi possível conectar à API de predição. Verifique se ela está rodando."
            return render(request, 'formulario/formulario.html', {'error': error_message})
        
        # 3. Redirecionar para a página de resultado
        return redirect('resultado:mostrar_resultado')

    # Se a requisição não for POST, redireciona de volta para o formulário
    return redirect('formulario:formulario_view')