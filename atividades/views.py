from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'atividades/index.html')


@login_required(login_url='/login')
def home(request):
    return render(request, 'atividades/home.html')


def sobre(request):
    return render(request, 'atividades/sobre.html')


def contato(request):
    return render(request, 'atividades/contato.html')


def sign_in(request):
    return render(request, 'atividades/login.html')


@csrf_protect
def submitlogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == '' and password == '':
            messages.error(request, 'Preencha todos os campos')
            return redirect('/login/')

        if username == '' and password != '':
            messages.error(request, 'Preencha o campo username')
            return redirect('/login/')

        if password == '' and username != '':
            messages.error(request, 'Preencha o campo password')
            return redirect('/login/')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
    return redirect('/')


def sair(request):
    print(request.user)
    logout(request)
    return redirect('/login/')


def portugues(request):
    return render(request, 'atividades/portugues/portugues.html')


def portuguesJogos(request):
    return render(request, 'atividades/portugues/jogos/jogos.html')


def portuguesJogosPrimeiroAno(request):
    return render(request, 'atividades/portugues/jogos/primeiroAno.html')


def portuguesJogosSegundoAno(request):
    return render(request, 'atividades/portugues/jogos/segundoAno.html')


def portuguesJogosTerceiroAno(request):
    return render(request, 'atividades/portugues/jogos/terceiroAno.html')


def portuguesJogosQuartoAno(request):
    return render(request, 'atividades/portugues/jogos/quartoAno.html')


def portuguesJogosQuintoAno(request):
    return render(request, 'atividades/portugues/jogos/quintoAno.html')


def portuguesAtividades(request):
    return render(request, 'atividades/portugues/atividade/atividades.html')


def portuguesAtividadesPrimeiroAno(request):
    return render(request, 'atividades/portugues/atividade/primeiroAno.html')


def portuguesAtividadesSegundoAno(request):
    return render(request, 'atividades/portugues/atividade/segundoAno.html')


def portuguesAtividadesTerceiroAno(request):
    return render(request, 'atividades/portugues/atividade/terceiroAno.html')


def portuguesAtividadesQuartoAno(request):
    return render(request, 'atividades/portugues/atividade/quartoAno.html')


def portuguesAtividadesQuintoAno(request):
    return render(request, 'atividades/portugues/atividade/quintoAno.html')


def portuguesVideos(request):
    return render(request, 'atividades/portugues/videos/videos.html')


def portuguesVideosPrimeiroAno(request):
    return render(request, 'atividades/portugues/video/primeiroAno.html')


def portuguesVideosSegundoAno(request):
    return render(request, 'atividades/portugues/video/segundoAno.html')


def portuguesVideosTerceiroAno(request):
    return render(request, 'atividades/portugues/video/terceiroAno.html')


def portuguesVideosQuartoAno(request):
    return render(request, 'atividades/portugues/video/quartoAno.html')


def portuguesVideosQuintoAno(request):
    return render(request, 'atividades/portugues/video/quintoAno.html')


def matematica(request):
    return render(request, 'atividades/matematica/matematica.html')


def matematicaJogos(request):
    return render(request, 'atividades/matematica/jogos/jogos.html')


def matematicaJogosPrimeiroAno(request):
    return render(request, 'atividades/matematica/jogos/primeiroAno.html')


def matematicaJogosSegundoAno(request):
    return render(request, 'atividades/matematica/jogos/segundoAno.html')


def matematicaJogosTerceiroAno(request):
    return render(request, 'atividades/matematica/jogos/terceiroAno.html')


def matematicaJogosQuartoAno(request):
    return render(request, 'atividades/matematica/jogos/quartoAno.html')


def matematicaJogosQuintoAno(request):
    return render(request, 'atividades/matematica/jogos/quintoAno.html')


def matematicaAtividades(request):
    return render(request, 'atividades/matematica/atividade/atividades.html')


def matAtivPrimeiroAno(request):
    return render(request, 'atividades/matematica/atividade/primeiroAno.html')


def matematicaAtividadesSegundoAno(request):
    return render(request, 'atividades/matematica/atividade/segundoAno.html')


def matAtivTerceiroAno(request):
    return render(request, 'atividades/matematica/atividade/terceiroAno.html')


def matematicaAtividadesQuartoAno(request):
    return render(request, 'atividades/matematica/atividade/quartoAno.html')


def matematicaAtividadesQuintoAno(request):
    return render(request, 'atividades/matematica/atividade/quintoAno.html')


def matematicaVideos(request):
    return render(request, 'atividades/matematica/videos/videos.html')


def matematicaVideosPrimeiroAno(request):
    return render(request, 'atividades/matematica/video/primeiroAno.html')


def matematicaVideosSegundoAno(request):
    return render(request, 'atividades/matematica/video/segundoAno.html')


def matematicaVideosTerceiroAno(request):
    return render(request, 'atividades/matematica/video/terceiroAno.html')


def matematicaVideosQuartoAno(request):
    return render(request, 'atividades/matematica/video/quartoAno.html')


def matematicaVideosQuintoAno(request):
    return render(request, 'atividades/matematica/video/quintoAno.html')


def historia(request):
    return render(request, 'atividades/historia/historia.html')


def historiaJogos(request):
    return render(request, 'atividades/historia/jogos/jogos.html')


def historiaJogosPrimeiroAno(request):
    return render(request, 'atividades/historia/jogos/primeiroAno.html')


def historiaJogosSegundoAno(request):
    return render(request, 'atividades/historia/jogos/segundoAno.html')


def historiaJogosTerceiroAno(request):
    return render(request, 'atividades/historia/jogos/terceiroAno.html')


def historiaJogosQuartoAno(request):
    return render(request, 'atividades/historia/jogos/quartoAno.html')


def historiaJogosQuintoAno(request):
    return render(request, 'atividades/historia/jogos/quintoAno.html')


def historiaAtividades(request):
    return render(request, 'atividades/historia/atividade/atividades.html')


def historiaAtividadesPrimeiroAno(request):
    return render(request, 'atividades/historia/atividade/primeiroAno.html')


def historiaAtividadesSegundoAno(request):
    return render(request, 'atividades/historia/atividade/segundoAno.html')


def historiaAtividadesTerceiroAno(request):
    return render(request, 'atividades/historia/atividade/terceiroAno.html')


def historiaAtividadesQuartoAno(request):
    return render(request, 'atividades/historia/atividade/quartoAno.html')


def historiaAtividadesQuintoAno(request):
    return render(request, 'atividades/historia/atividade/quintoAno.html')


def historiaVideos(request):
    return render(request, 'atividades/historia/videos/videos.html')


def historiaVideosPrimeiroAno(request):
    return render(request, 'atividades/historia/video/primeiroAno.html')


def historiaVideosSegundoAno(request):
    return render(request, 'atividades/historia/video/segundoAno.html')


def historiaVideosTerceiroAno(request):
    return render(request, 'atividades/historia/video/terceiroAno.html')


def historiaVideosQuartoAno(request):
    return render(request, 'atividades/historia/video/quartoAno.html')


def historiaVideosQuintoAno(request):
    return render(request, 'atividades/historia/video/quintoAno.html')


def geografia(request):
    return render(request, 'atividades/geografia/geografia.html')


def geografiaJogos(request):
    return render(request, 'atividades/geografia/jogos/jogos.html')


def geografiaJogosPrimeiroAno(request):
    return render(request, 'atividades/geografia/jogos/primeiroAno.html')


def geografiaJogosSegundoAno(request):
    return render(request, 'atividades/geografia/jogos/segundoAno.html')


def geografiaJogosTerceiroAno(request):
    return render(request, 'atividades/geografia/jogos/terceiroAno.html')


def geografiaJogosQuartoAno(request):
    return render(request, 'atividades/geografia/jogos/quartoAno.html')


def geografiaJogosQuintoAno(request):
    return render(request, 'atividades/geografia/jogos/quintoAno.html')


def geografiaAtividades(request):
    return render(request, 'atividades/geografia/atividade/atividades.html')


def geografiaAtividadesPrimeiroAno(request):
    return render(request, 'atividades/geografia/atividade/primeiroAno.html')


def geografiaAtividadesSegundoAno(request):
    return render(request, 'atividades/geografia/atividade/segundoAno.html')


def geografiaAtividadesTerceiroAno(request):
    return render(request, 'atividades/geografia/atividade/terceiroAno.html')


def geografiaAtividadesQuartoAno(request):
    return render(request, 'atividades/geografia/atividade/quartoAno.html')


def geografiaAtividadesQuintoAno(request):
    return render(request, 'atividades/geografia/atividade/quintoAno.html')


def geografiaVideos(request):
    return render(request, 'atividades/geografia/videos/videos.html')


def geografiaVideosPrimeiroAno(request):
    return render(request, 'atividades/geografia/video/primeiroAno.html')


def geografiaVideosSegundoAno(request):
    return render(request, 'atividades/geografia/video/segundoAno.html')


def geografiaVideosTerceiroAno(request):
    return render(request, 'atividades/geografia/video/terceiroAno.html')


def geografiaVideosQuartoAno(request):
    return render(request, 'atividades/geografia/video/quartoAno.html')


def geografiaVideosQuintoAno(request):
    return render(request, 'atividades/geografia/video/quintoAno.html')


def ciencias(request):
    return render(request, 'atividades/ciencias/ciencias.html')


def cienciasJogos(request):
    return render(request, 'atividades/ciencias/jogos/jogos.html')


def cienciasJogosPrimeiroAno(request):
    return render(request, 'atividades/ciencias/jogos/primeiroAno.html')


def cienciasJogosSegundoAno(request):
    return render(request, 'atividades/ciencias/jogos/segundoAno.html')


def cienciasJogosTerceiroAno(request):
    return render(request, 'atividades/ciencias/jogos/terceiroAno.html')


def cienciasJogosQuartoAno(request):
    return render(request, 'atividades/ciencias/jogos/quartoAno.html')


def cienciasJogosQuintoAno(request):
    return render(request, 'atividades/ciencias/jogos/quintoAno.html')


def cienciasAtividades(request):
    return render(request, 'atividades/ciencias/atividade/atividades.html')


def cienciasAtividadesPrimeiroAno(request):
    return render(request, 'atividades/ciencias/atividade/primeiroAno.html')


def cienciasAtividadesSegundoAno(request):
    return render(request, 'atividades/ciencias/atividade/segundoAno.html')


def cienciasAtividadesTerceiroAno(request):
    return render(request, 'atividades/ciencias/atividade/terceiroAno.html')


def cienciasAtividadesQuartoAno(request):
    return render(request, 'atividades/ciencias/atividade/quartoAno.html')


def cienciasAtividadesQuintoAno(request):
    return render(request, 'atividades/ciencias/atividade/quintoAno.html')


def cienciasVideos(request):
    return render(request, 'atividades/ciencias/videos/videos.html')


def cienciasVideosPrimeiroAno(request):
    return render(request, 'atividades/ciencias/video/primeiroAno.html')


def cienciasVideosSegundoAno(request):
    return render(request, 'atividades/ciencias/video/segundoAno.html')


def cienciasVideosTerceiroAno(request):
    return render(request, 'atividades/ciencias/video/terceiroAno.html')


def cienciasVideosQuartoAno(request):
    return render(request, 'atividades/ciencias/video/quartoAno.html')


def cienciasVideosQuintoAno(request):
    return render(request, 'atividades/ciencias/video/quintoAno.html')


def ingles(request):
    return render(request, 'atividades/ingles/ingles.html')


def inglesJogos(request):
    return render(request, 'atividades/ingles/jogos/jogos.html')


def inglesJogosPrimeiroAno(request):
    return render(request, 'atividades/ingles/jogos/primeiroAno.html')


def inglesJogosSegundoAno(request):
    return render(request, 'atividades/ingles/jogos/segundoAno.html')


def inglesJogosTerceiroAno(request):
    return render(request, 'atividades/ingles/jogos/terceiroAno.html')


def inglesJogosQuartoAno(request):
    return render(request, 'atividades/ingles/jogos/quartoAno.html')


def inglesJogosQuintoAno(request):
    return render(request, 'atividades/ingles/jogos/quintoAno.html')


def inglesAtividades(request):
    return render(request, 'atividades/ingles/atividade/atividades.html')


def inglesAtividadesPrimeiroAno(request):
    return render(request, 'atividades/ingles/atividade/primeiroAno.html')


def inglesAtividadesSegundoAno(request):
    return render(request, 'atividades/ingles/atividade/segundoAno.html')


def inglesAtividadesTerceiroAno(request):
    return render(request, 'atividades/ingles/atividade/terceiroAno.html')


def inglesAtividadesQuartoAno(request):
    return render(request, 'atividades/ingles/atividade/quartoAno.html')


def inglesAtividadesQuintoAno(request):
    return render(request, 'atividades/ingles/atividade/quintoAno.html')


def inglesVideos(request):
    return render(request, 'atividades/ingles/videos/videos.html')


def inglesVideosPrimeiroAno(request):
    return render(request, 'atividades/ingles/video/primeiroAno.html')


def inglesVideosSegundoAno(request):
    return render(request, 'atividades/ingles/video/segundoAno.html')


def inglesVideosTerceiroAno(request):
    return render(request, 'atividades/ingles/video/terceiroAno.html')


def inglesVideosQuartoAno(request):
    return render(request, 'atividades/ingles/video/quartoAno.html')


def inglesVideosQuintoAno(request):
    return render(request, 'atividades/ingles/video/quintoAno.html')
