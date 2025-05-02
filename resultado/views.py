from django.shortcuts import render

def mostrar_resultado(request):
    if request.method == 'POST':
        resultado = request.POST.get('resultado')  # vem como string '0' ou '1'
        contexto = {
            'positivo': resultado == '0'
        }
        return render(request, 'resultado/resultado.html', contexto)
