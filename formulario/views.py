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
