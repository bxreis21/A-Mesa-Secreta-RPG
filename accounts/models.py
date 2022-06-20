from django.db import models
from django.contrib.auth.models import User

class Conta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField(max_length=50, default=user.first_name ,verbose_name='Nome')
    sobrenome = models.CharField(max_length=50, default=user.last_name, verbose_name='Sobrenome')
    nick = models.CharField(max_length=50, verbose_name='Nickname')




# Create your models here.
