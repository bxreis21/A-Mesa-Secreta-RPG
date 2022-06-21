from django.shortcuts import redirect, render
from .models import Ficha, Personagen, Atributo

def dashboard(request):
    return render(request, 'dashboard.html')

def ficha(request):
    if request.method !='POST':
        print('no post')
        return render(request, 'ficha.html')

    nome_personagem = request.POST.get('nome_personagem')
    origem = request.POST.get('origem')
    classe = request.POST.get('classe')
    nex = request.POST.get('nex')
    patente = request.POST.get('patente')
    personagen = Personagen.objects.create(nome=nome_personagem,origem=origem,nex=nex,patente=patente,classe=classe)
    personagen.save()

    forca = request.POST.get('forca')
    agilidade = request.POST.get('agilidade')
    inteligencia = request.POST.get('inteligencia')
    presenca = request.POST.get('presenca')
    vigor = request.POST.get('vigor')
    atributo = Atributo.objects.create(forca=forca, agilidade=agilidade,inteligencia=inteligencia,vigor=vigor,presenca=presenca)
    atributo.save()

    ficha = Ficha.objects.create(personagem=personagen,atributos=atributo)
    ficha.save()

    return redirect('dashboard')

def mesa(request):
    pass
# Create your views here.
