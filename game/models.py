from django.db import models
from django.contrib.auth.models import User


class Pericias(models.Model):
    pass

class Atributo(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    forca = models.IntegerField(verbose_name='Força', blank=True, null=True)
    agilidade = models.IntegerField(verbose_name='Agilidade', blank=True, null=True)
    inteligencia = models.IntegerField(verbose_name='Inteligência', blank=True, null=True)
    vigor = models.IntegerField(verbose_name='Vigor', blank=True, null=True)
    presenca = models.IntegerField(verbose_name='Presença', blank=True, null=True)

    def __str__(self):
        return f'{self.id}'

class Personagen(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    nome = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nome' )
    origem = models.CharField(max_length=50, blank=True, null=True, verbose_name='Origem')
    nex = models.CharField(max_length=50, blank=True, null=True, verbose_name='Nível de Exposição Paranormal')
    patente = models.CharField(max_length=50, blank=True, null=True, verbose_name='Patente')
    classe = models.CharField(max_length=30, blank=True, null= True, verbose_name='Classe')

    def __str__(self):
        return f'{self.id}-{self.nome}-{self.classe}'

class Ficha(models.Model):
    id = models.BigAutoField(primary_key=True,auto_created=True)
    mestre = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True,null=True, verbose_name='Mestre' , related_name='mestre')
    jogador = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True,null=True, verbose_name='Jogador', related_name='jogador')
    personagem = models.ForeignKey(Personagen,on_delete=models.CASCADE, verbose_name='Informações Gerais')
    atributos = models.ForeignKey(Atributo, on_delete=models.CASCADE, verbose_name='Atributos')

    def __str__(self): 
        return f'{self.id}-Jogador:{self.jogador}, Mestre: {self.mestre}'


    
# Create your models here.
