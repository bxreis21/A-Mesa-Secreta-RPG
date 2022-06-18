from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth


def Index(request):
    return render(request, 'index.html')

def Login(request):
    if request.method != 'post':
        return render(request, 'login.html')


    usuario = request.POST.get('login')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario,password=senha)

    if not user:
        print('Preencha os campos!')
        return render(request, 'login.html')
    
    else:
        auth.login(request, user)
        print('sucesso')
        return redirect('index')


def Register(request):
    if request.method == 'post':
        print('method no post')
        return render(request, 'register.html')
    
    user = request.POST.get('usuario')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    idade = request.POST.get('idade')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')


    if not user or not nome or not sobrenome or not idade or not email or not senha or not senha2:
        print('Preencha todos os campos!')
        return render(request, 'register.html')

    try:
        validate_email(email)

    except ValidationError:
        print('Email Inválido!')
        return render(request, 'register.html')

    if senha != senha2: 
        print('As senhas devem ser iguais!')
        return render(request, 'register.html')
    
    if idade <= 16:
        print('Idade mínima para criar conta é de 16 anos.')

    if User.objects.filter(username='usuario').exists():
        print('O Usuario já existe.')
        return render(request, 'register.html')

    if User.objects.filter(email='email').exists():
        print('O email já existe.')
        return render(request, 'register.html')

    user = User.objects.create_user(username=user, nome=nome, sobrenome=sobrenome,idade=idade, email=email, password=senha)
    user.save()

    print('usuario logado com sucesso!')


    
# Create your views here.
