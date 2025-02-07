from django.shortcuts import render
from django.http import HttpResponse
from .models import NomeResponsavel

# Create your views here.
def HomeView(request):
    if request.method == "GET":
        nome_responsavel = NomeResponsavel.objects.all()
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')

        responsavel = NomeResponsavel(
            nome=nome,
            sobrenome=sobrenome
            )
        responsavel.save()

        nome_responsavel = NomeResponsavel.objects.all()
    return render(request, 'index.html')

def ListaresponsaveisView(request):
    if request.method == "GET":
        lista_responsaveis = NomeResponsavel.objects.all()
        return render (request, 'listaresponsaveis.html',{'responsaveis':lista_responsaveis})
    
def AtualizaresponsavelView(request, id):
    if request.method == 'GET':
        responsavel = NomeResponsavel.objects.get(id=id)
        return render (request, 'atualizaresponsavel.html', {'responsavel': responsavel})