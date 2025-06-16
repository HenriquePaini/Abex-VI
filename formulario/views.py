"""
from django.shortcuts import render, redirect
from .models import DadosDiabetes

def resultado(request):
    return render(request, 'resultado/resultado.html')

def formulario_view(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        gravidez = request.POST.get('gravidez') or None
        glicose = request.POST.get('glicose')
        pressao = request.POST.get('pressao')
        espessura_pele = request.POST.get('espessura_pele')
        insulina = request.POST.get('insulina')
        imc = request.POST.get('imc')
        pedigree = request.POST.get('pedigree')
        idade = request.POST.get('idade')
        resultado = request.POST.get('resultado')

        # Cria e salva no banco secundário
        DadosDiabetes.objects.using('formulario_db').create(
            gravidez=gravidez,
            glicose=glicose,
            pressao=pressao,
            espessura_pele=espessura_pele,
            insulina=insulina,
            imc=imc,
            pedigree=pedigree,
            idade=idade,
            resultado=resultado
        )

        return render(request, 'formulario/formulario.html', {
            'mensagem': 'Dados enviados com sucesso!'
        })

    return render(request, 'formulario/formulario.html')







"""
# Arquivo: GLYCOSENSE/formulario/views.py

from django.shortcuts import render, redirect
from .models import DadosDiabetes

# Esta view tem UMA responsabilidade: MOSTRAR a página com o formulário.
def formulario_view(request):
    # Apenas renderiza o template do formulário.
    return render(request, 'formulario/formulario.html')

# Esta view tem DUAS responsabilidades: RECEBER os dados e SALVAR, e depois MOSTRAR o resultado.
def resultado(request):
    # Esta lógica só executa quando o formulário é enviado (método POST).
    if request.method == 'POST':
        try:
            # --- 1. CAPTURA E SALVA OS DADOS NO BANCO DE DADOS ---
            # Cria uma nova instância do seu modelo com os dados do formulário.
            novo_dado = DadosDiabetes(
                gravidez=int(request.POST.get('gravidez')),
                glicose=int(request.POST.get('glicose')),
                pressao=int(request.POST.get('pressao')),
                espessura_pele=int(request.POST.get('espessura_pele')),
                insulina=int(request.POST.get('insulina')),
                imc=float(request.POST.get('imc')),
                pedigree=float(request.POST.get('pedigree')),
                idade=int(request.POST.get('idade')),
                resultado=int(request.POST.get('resultado'))
            )

            # Salva o objeto no banco de dados correto, como definido no seu DBRouter.
            novo_dado.save(using='formulario_db')

            print("SUCESSO: Novo dado salvo no banco de dados!")

            # --- 2. PREPARA PARA MOSTRAR A PÁGINA DE RESULTADO ---
            # Por enquanto, vamos apenas confirmar que foi salvo.
            # A lógica do modelo de ML virá aqui depois.
            context = {
                'mensagem': 'Dados salvos com sucesso!',
                'novo_dado': novo_dado 
            }

            # Renderiza a página de resultado com uma mensagem de sucesso.
            return render(request, 'resultado/resultado.html', context)

        except (ValueError, TypeError) as e:
            # Se houver um erro nos dados (ex: texto em campo de número),
            # volta para o formulário com uma mensagem de erro.
            print(f"ERRO ao processar formulário: {e}")
            return render(request, 'formulario/formulario.html', {'error': 'Dados inválidos. Por favor, verifique os valores inseridos.'})

    # Se alguém tentar acessar a URL /resultado diretamente (sem enviar dados),
    # ele será redirecionado de volta para a página do formulário.
    return redirect('formularios:formulario')
