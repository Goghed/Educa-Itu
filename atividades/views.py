from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/login')
def home(request):
    return render(request, 'atividades/home.html')


def sign_in(request):
    return render(request, 'atividades/login.html')


@csrf_protect
def submit_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password == '':
            messages.error(request, 'Preencha todos os campos')
            return redirect('/login')

        if username == '' and password != '':
            messages.error(request, 'Preencha o campo username')
            return redirect('/login')

        if password == '' and username != '':
            messages.error(request, 'Preencha o campo password')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
    return redirect('/login/')


def sair(request):
    print(request.user)
    logout(request)
    return redirect('/login/')


def portugues(request):
    return render(request, 'atividades/portugues.html')


def matematica(request):
    return render(request, 'atividades/matematica.html')


def historia(request):
    return render(request, 'atividades/historia.html')


def geografia(request):
    return render(request, 'atividades/geografia.html')


def ciencias(request):
    return render(request, 'atividades/ciencias.html')


def ingles(request):
    return render(request, 'atividades/ingles.html')


def jogos(request):
    return render(request, 'atividades/jogos.html')


def videos(request):
    return render(request, 'atividades/videos.html')


def atividades(request):
    return render(request, 'atividades/atividades.html')
