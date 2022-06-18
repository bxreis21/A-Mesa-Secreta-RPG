from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from . import models

def Index(request):
    return render(request, 'index.html')

class Login(ListView):
    model = models.Accounts
    template_name = 'login.html'    

class Register(Login):
    template_name = 'register.html'

    
# Create your views here.
