from django.db import models
from django.contrib.auth.models import User


class Pericias(models.Model):
    pass

class Atributos(models.Model):
    força = models.IntegerField(verbose_name='Força')
    agilidade = models.IntegerField(verbose_name='Agilidade')
    inteligencia = models.IntegerField(verbose_name='Inteligência')
    vigor = models.IntegerField(verbose_name='Vigor')
    presença = models.IntegerField(verbose_name='Presença')

class Info_Gerais(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome' )
    origem = models.CharField(max_length=50, blank=True, null=True, verbose_name='Origem')
    nex = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nível de Exposição Paranormal')
    patente = models.CharField(max_length=50, blank=True, null=True, verbose_name='Patente')

class Ficha(models.Model):
    mestre = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, verbose_name='Mestre') 
    info_gerais = models.ForeignKey(Info_Gerais,on_delete=models.DO_NOTHING, verbose_name='Informações Gerais')
    atributos = models.ForeignKey(Atributos, on_delete=models.DO_NOTHING, verbose_name='Atributos')


    
# Create your models here.
