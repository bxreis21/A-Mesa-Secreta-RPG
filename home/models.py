from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='User')
    nome = models.CharField(max_length=50, verbose_name='Nome')
    sobrenome = models.CharField(max_length=50, verbose_name='Sobrenome')
    email = models.EmailField(verbose_name='E-mail')
    idade = models.IntegerField(verbose_name='Idade')
    senha = models.CharField(max_length=50, verbose_name='Senha')

    def __str__(self):
        return f'{self.nome}'

# Create your models here.
