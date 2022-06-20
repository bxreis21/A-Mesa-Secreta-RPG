from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method != 'POST':
        print('no post')
        return render(request, 'login.html')

    usuario = request.POST.get('login')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario,password=senha)

    if not user:
        messages.error(request, 'Usuário e/ou senha não encontrados na base de dados.')
        return redirect('login')
    
    else:
        auth.login(request, user)
        messages.success(request, 'Logado com sucesso!')
        return redirect('index')


def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    
    user = request.POST.get('usuario')
    nome_completo = request.POST.get('nome_completo')
    idade = request.POST.get('idade')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    nome_completo = nome_completo.strip(' ').lower().title().split(' ')
    nome = nome_completo[0]
    sobrenome = ' '.join(nome_completo[1:]).lower().title().strip()

    print(nome_completo)
    print(nome)
    print(sobrenome)


    if not user or not nome_completo or not idade or not email or not senha or not senha2:
        messages.error(request, 'Preencha os campos!')
        return render(request, 'register.html')

    try:
        validate_email(email)

    except ValidationError:
        messages.error(request,'Email inválido.')
        return render(request, 'register.html')

    if senha != senha2: 
        messages.error(request, 'As senhas devem ser iguais')
        return render(request, 'register.html')

    if len(senha) < 5:
        messages.error(request, 'A senha precisa ter pelo menos 5 caracteres' )
        return render(request, 'register.html')

    if int(idade) <= 16:
        messages.error(request,'Idade mínima para criar conta é de 16 anos.')
        return render(request, 'register.html')

    if User.objects.filter(username=user).exists():
        messages.error(request, 'O nome de usuário já existe.')
        return render(request, 'register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'O email escolhido já possui uma conta no nosso site.')
        return render(request, 'register.html')

    user = User.objects.create_user(username=user, first_name=nome, last_name=sobrenome, email=email, password=senha)
    user.save()
    messages.success(request, 'Usuário logado com sucesso.')
    return redirect('login')


@login_required
def log_out(request):
    logout(request)
    return redirect('index')
