from django.shortcuts import render, redirect
from .models import Lanche
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


def cardapio(request):
    dados = Lanche.objects.order_by('id')
    return render(request, 'cardapio.html', {'dados':dados})

def login(request):
    # ! validando se veio de um formulario
    if request.method != 'POST':
        return render(request, 'login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.add_message(request, messages.ERROR, 'Usuário ou senha inválido')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        return redirect('servicos')

def logout(request):
    auth.logout(request)
    return redirect('home')

def register(request):
    #! validando se veio de um formulario
    if request.method != 'POST':
        return render(request, 'register.html')

    #! obtendo os valores do formulario
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    senha1 = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    #! verificando se ha campos vazios
    if not email or not usuario or not nome or not sobrenome or not senha1 or not senha2:
        messages.add_message(request, messages.WARNING, 'Todos os campos devem estar preenchidos!!!')
        return render(request, 'register.html')

    #! validando informações dos campos
    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.ERROR, 'Email Inválido!!!')
        return render(request, 'register.html')

    if len(senha1) < 6:
        messages.add_message(request, messages.WARNING, 'Senha deve conter no minimo 6 caracteres!!!')
        return render(request, 'register.html')

    if senha1 != senha2:
        messages.add_message(request, messages.WARNING, 'Senhas são diferentes!!!')
        return render(request, 'register.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.WARNING, 'Usuário já existe!!!')
        return render(request, 'register.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.WARNING, 'Email já existe!!!')
        return render(request, 'register.html')

    user = User.objects.create_user(username=usuario, email=email, first_name=nome, last_name=sobrenome, password=senha1)

    messages.add_message(request, messages.SUCCESS, 'Cadastrado com Sucesso!!!')
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def servicos(request):
        return render(request, 'servicos.html')

