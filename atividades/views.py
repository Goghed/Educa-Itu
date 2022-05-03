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
    return render(request, 'atividades/inicial/home.html')


def sobreLogado(request):
    return render(request, 'atividades/inicial/sobre.html')


def contatoLogado(request):
    return render(request, 'atividades/inicial/contato.html')


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


@login_required(login_url='/login')
def portugues(request):
    return render(request, 'atividades/portugues/portugues.html')


@login_required(login_url='/login')
def portuguesJogos(request):
    return render(request, 'atividades/portugues/jogos/jogos.html')


@login_required(login_url='/login')
def portuguesJogosPrimeiroAno(request):
    return render(request, 'atividades/portugues/jogos/primeiroAno.html')


@login_required(login_url='/login')
def portuguesJogosSegundoAno(request):
    return render(request, 'atividades/portugues/jogos/segundoAno.html')


@login_required(login_url='/login')
def portuguesJogosTerceiroAno(request):
    return render(request, 'atividades/portugues/jogos/terceiroAno.html')


@login_required(login_url='/login')
def portuguesJogosQuartoAno(request):
    return render(request, 'atividades/portugues/jogos/quartoAno.html')


@login_required(login_url='/login')
def portuguesJogosQuintoAno(request):
    return render(request, 'atividades/portugues/jogos/quintoAno.html')


@login_required(login_url='/login')
def portuguesAtividades(request):
    return render(request, 'atividades/portugues/atividade/atividades.html')


@login_required(login_url='/login')
def portuguesAtividadesPrimeiroAno(request):
    return render(request, 'atividades/portugues/atividade/primeiroAno.html')


@login_required(login_url='/login')
def portuguesAtividadesSegundoAno(request):
    return render(request, 'atividades/portugues/atividade/segundoAno.html')


@login_required(login_url='/login')
def portuguesAtividadesTerceiroAno(request):
    return render(request, 'atividades/portugues/atividade/terceiroAno.html')


@login_required(login_url='/login')
def portuguesAtividadesQuartoAno(request):
    return render(request, 'atividades/portugues/atividade/quartoAno.html')


@login_required(login_url='/login')
def portuguesAtividadesQuintoAno(request):
    return render(request, 'atividades/portugues/atividade/quintoAno.html')


@login_required(login_url='/login')
def portuguesVideos(request):
    return render(request, 'atividades/portugues/videos/videos.html')


@login_required(login_url='/login')
def portuguesVideosPrimeiroAno(request):
    return render(request, 'atividades/portugues/videos/primeiroAno.html')


@login_required(login_url='/login')
def portuguesVideosSegundoAno(request):
    return render(request, 'atividades/portugues/videos/segundoAno.html')


@login_required(login_url='/login')
def portuguesVideosTerceiroAno(request):
    return render(request, 'atividades/portugues/videos/terceiroAno.html')


@login_required(login_url='/login')
def portuguesVideosQuartoAno(request):
    return render(request, 'atividades/portugues/videos/quartoAno.html')


@login_required(login_url='/login')
def portuguesVideosQuintoAno(request):
    return render(request, 'atividades/portugues/videos/quintoAno.html')


@login_required(login_url='/login')
def matematica(request):
    return render(request, 'atividades/matematica/matematica.html')


@login_required(login_url='/login')
def matematicaJogos(request):
    return render(request, 'atividades/matematica/jogos/jogos.html')


@login_required(login_url='/login')
def matematicaJogosPrimeiroAno(request):
    return render(request, 'atividades/matematica/jogos/primeiroAno.html')


@login_required(login_url='/login')
def matematicaJogosSegundoAno(request):
    return render(request, 'atividades/matematica/jogos/segundoAno.html')


@login_required(login_url='/login')
def matematicaJogosTerceiroAno(request):
    return render(request, 'atividades/matematica/jogos/terceiroAno.html')


@login_required(login_url='/login')
def matematicaJogosQuartoAno(request):
    return render(request, 'atividades/matematica/jogos/quartoAno.html')


@login_required(login_url='/login')
def matematicaJogosQuintoAno(request):
    return render(request, 'atividades/matematica/jogos/quintoAno.html')


@login_required(login_url='/login')
def matematicaAtividades(request):
    return render(request, 'atividades/matematica/atividade/atividades.html')


@login_required(login_url='/login')
def matAtivPrimeiroAno(request):
    return render(request, 'atividades/matematica/atividade/primeiroAno.html')


@login_required(login_url='/login')
def matematicaAtividadesSegundoAno(request):
    return render(request, 'atividades/matematica/atividade/segundoAno.html')


@login_required(login_url='/login')
def matAtivTerceiroAno(request):
    return render(request, 'atividades/matematica/atividade/terceiroAno.html')


@login_required(login_url='/login')
def matematicaAtividadesQuartoAno(request):
    return render(request, 'atividades/matematica/atividade/quartoAno.html')


@login_required(login_url='/login')
def matematicaAtividadesQuintoAno(request):
    return render(request, 'atividades/matematica/atividade/quintoAno.html')


@login_required(login_url='/login')
def matematicaVideos(request):
    return render(request, 'atividades/matematica/videos/videos.html')


@login_required(login_url='/login')
def matematicaVideosPrimeiroAno(request):
    return render(request, 'atividades/matematica/videos/primeiroAno.html')


@login_required(login_url='/login')
def matematicaVideosSegundoAno(request):
    return render(request, 'atividades/matematica/videos/segundoAno.html')


@login_required(login_url='/login')
def matematicaVideosTerceiroAno(request):
    return render(request, 'atividades/matematica/videos/terceiroAno.html')


@login_required(login_url='/login')
def matematicaVideosQuartoAno(request):
    return render(request, 'atividades/matematica/videos/quartoAno.html')


@login_required(login_url='/login')
def matematicaVideosQuintoAno(request):
    return render(request, 'atividades/matematica/videos/quintoAno.html')


@login_required(login_url='/login')
def historia(request):
    return render(request, 'atividades/historia/historia.html')


@login_required(login_url='/login')
def historiaJogos(request):
    return render(request, 'atividades/historia/jogos/jogos.html')


@login_required(login_url='/login')
def historiaJogosPrimeiroAno(request):
    return render(request, 'atividades/historia/jogos/primeiroAno.html')


@login_required(login_url='/login')
def historiaJogosSegundoAno(request):
    return render(request, 'atividades/historia/jogos/segundoAno.html')


@login_required(login_url='/login')
def historiaJogosTerceiroAno(request):
    return render(request, 'atividades/historia/jogos/terceiroAno.html')


@login_required(login_url='/login')
def historiaJogosQuartoAno(request):
    return render(request, 'atividades/historia/jogos/quartoAno.html')


@login_required(login_url='/login')
def historiaJogosQuintoAno(request):
    return render(request, 'atividades/historia/jogos/quintoAno.html')


@login_required(login_url='/login')
def historiaAtividades(request):
    return render(request, 'atividades/historia/atividade/atividades.html')


@login_required(login_url='/login')
def historiaAtividadesPrimeiroAno(request):
    return render(request, 'atividades/historia/atividade/primeiroAno.html')


@login_required(login_url='/login')
def historiaAtividadesSegundoAno(request):
    return render(request, 'atividades/historia/atividade/segundoAno.html')


@login_required(login_url='/login')
def historiaAtividadesTerceiroAno(request):
    return render(request, 'atividades/historia/atividade/terceiroAno.html')


@login_required(login_url='/login')
def historiaAtividadesQuartoAno(request):
    return render(request, 'atividades/historia/atividade/quartoAno.html')


@login_required(login_url='/login')
def historiaAtividadesQuintoAno(request):
    return render(request, 'atividades/historia/atividade/quintoAno.html')


@login_required(login_url='/login')
def historiaVideos(request):
    return render(request, 'atividades/historia/videos/videos.html')


@login_required(login_url='/login')
def historiaVideosPrimeiroAno(request):
    return render(request, 'atividades/historia/videos/primeiroAno.html')


@login_required(login_url='/login')
def historiaVideosSegundoAno(request):
    return render(request, 'atividades/historia/videos/segundoAno.html')


@login_required(login_url='/login')
def historiaVideosTerceiroAno(request):
    return render(request, 'atividades/historia/videos/terceiroAno.html')


@login_required(login_url='/login')
def historiaVideosQuartoAno(request):
    return render(request, 'atividades/historia/videos/quartoAno.html')


@login_required(login_url='/login')
def historiaVideosQuintoAno(request):
    return render(request, 'atividades/historia/videos/quintoAno.html')


@login_required(login_url='/login')
def geografia(request):
    return render(request, 'atividades/geografia/geografia.html')


@login_required(login_url='/login')
def geografiaJogos(request):
    return render(request, 'atividades/geografia/jogos/jogos.html')


@login_required(login_url='/login')
def geografiaJogosPrimeiroAno(request):
    return render(request, 'atividades/geografia/jogos/primeiroAno.html')


@login_required(login_url='/login')
def geografiaJogosSegundoAno(request):
    return render(request, 'atividades/geografia/jogos/segundoAno.html')


@login_required(login_url='/login')
def geografiaJogosTerceiroAno(request):
    return render(request, 'atividades/geografia/jogos/terceiroAno.html')


@login_required(login_url='/login')
def geografiaJogosQuartoAno(request):
    return render(request, 'atividades/geografia/jogos/quartoAno.html')


@login_required(login_url='/login')
def geografiaJogosQuintoAno(request):
    return render(request, 'atividades/geografia/jogos/quintoAno.html')


@login_required(login_url='/login')
def geografiaAtividades(request):
    return render(request, 'atividades/geografia/atividade/atividades.html')


@login_required(login_url='/login')
def geografiaAtividadesPrimeiroAno(request):
    return render(request, 'atividades/geografia/atividade/primeiroAno.html')


@login_required(login_url='/login')
def geografiaAtividadesSegundoAno(request):
    return render(request, 'atividades/geografia/atividade/segundoAno.html')


@login_required(login_url='/login')
def geografiaAtividadesTerceiroAno(request):
    return render(request, 'atividades/geografia/atividade/terceiroAno.html')


@login_required(login_url='/login')
def geografiaAtividadesQuartoAno(request):
    return render(request, 'atividades/geografia/atividade/quartoAno.html')


@login_required(login_url='/login')
def geografiaAtividadesQuintoAno(request):
    return render(request, 'atividades/geografia/atividade/quintoAno.html')


@login_required(login_url='/login')
def geografiaVideos(request):
    return render(request, 'atividades/geografia/videos/videos.html')


@login_required(login_url='/login')
def geografiaVideosPrimeiroAno(request):
    return render(request, 'atividades/geografia/videos/primeiroAno.html')


@login_required(login_url='/login')
def geografiaVideosSegundoAno(request):
    return render(request, 'atividades/geografia/videos/segundoAno.html')


@login_required(login_url='/login')
def geografiaVideosTerceiroAno(request):
    return render(request, 'atividades/geografia/videos/terceiroAno.html')


@login_required(login_url='/login')
def geografiaVideosQuartoAno(request):
    return render(request, 'atividades/geografia/videos/quartoAno.html')


@login_required(login_url='/login')
def geografiaVideosQuintoAno(request):
    return render(request, 'atividades/geografia/videos/quintoAno.html')


@login_required(login_url='/login')
def ciencias(request):
    return render(request, 'atividades/ciencias/ciencias.html')


@login_required(login_url='/login')
def cienciasJogos(request):
    return render(request, 'atividades/ciencias/jogos/jogos.html')


@login_required(login_url='/login')
def cienciasJogosPrimeiroAno(request):
    return render(request, 'atividades/ciencias/jogos/primeiroAno.html')


@login_required(login_url='/login')
def cienciasJogosSegundoAno(request):
    return render(request, 'atividades/ciencias/jogos/segundoAno.html')


@login_required(login_url='/login')
def cienciasJogosTerceiroAno(request):
    return render(request, 'atividades/ciencias/jogos/terceiroAno.html')


@login_required(login_url='/login')
def cienciasJogosQuartoAno(request):
    return render(request, 'atividades/ciencias/jogos/quartoAno.html')


@login_required(login_url='/login')
def cienciasJogosQuintoAno(request):
    return render(request, 'atividades/ciencias/jogos/quintoAno.html')


@login_required(login_url='/login')
def cienciasAtividades(request):
    return render(request, 'atividades/ciencias/atividade/atividades.html')


@login_required(login_url='/login')
def cienciasAtividadesPrimeiroAno(request):
    return render(request, 'atividades/ciencias/atividade/primeiroAno.html')


@login_required(login_url='/login')
def cienciasAtividadesSegundoAno(request):
    return render(request, 'atividades/ciencias/atividade/segundoAno.html')


@login_required(login_url='/login')
def cienciasAtividadesTerceiroAno(request):
    return render(request, 'atividades/ciencias/atividade/terceiroAno.html')


@login_required(login_url='/login')
def cienciasAtividadesQuartoAno(request):
    return render(request, 'atividades/ciencias/atividade/quartoAno.html')


@login_required(login_url='/login')
def cienciasAtividadesQuintoAno(request):
    return render(request, 'atividades/ciencias/atividade/quintoAno.html')


@login_required(login_url='/login')
def cienciasVideos(request):
    return render(request, 'atividades/ciencias/videos/videos.html')


@login_required(login_url='/login')
def cienciasVideosPrimeiroAno(request):
    return render(request, 'atividades/ciencias/videos/primeiroAno.html')


@login_required(login_url='/login')
def cienciasVideosSegundoAno(request):
    return render(request, 'atividades/ciencias/videos/segundoAno.html')


@login_required(login_url='/login')
def cienciasVideosTerceiroAno(request):
    return render(request, 'atividades/ciencias/videos/terceiroAno.html')


@login_required(login_url='/login')
def cienciasVideosQuartoAno(request):
    return render(request, 'atividades/ciencias/videos/quartoAno.html')


@login_required(login_url='/login')
def cienciasVideosQuintoAno(request):
    return render(request, 'atividades/ciencias/videos/quintoAno.html')


@login_required(login_url='/login')
def ingles(request):
    return render(request, 'atividades/ingles/ingles.html')


@login_required(login_url='/login')
def inglesJogos(request):
    return render(request, 'atividades/ingles/jogos/jogos.html')


@login_required(login_url='/login')
def inglesJogosPrimeiroAno(request):
    return render(request, 'atividades/ingles/jogos/primeiroAno.html')


@login_required(login_url='/login')
def inglesJogosSegundoAno(request):
    return render(request, 'atividades/ingles/jogos/segundoAno.html')


@login_required(login_url='/login')
def inglesJogosTerceiroAno(request):
    return render(request, 'atividades/ingles/jogos/terceiroAno.html')


@login_required(login_url='/login')
def inglesJogosQuartoAno(request):
    return render(request, 'atividades/ingles/jogos/quartoAno.html')


@login_required(login_url='/login')
def inglesJogosQuintoAno(request):
    return render(request, 'atividades/ingles/jogos/quintoAno.html')


@login_required(login_url='/login')
def inglesAtividades(request):
    return render(request, 'atividades/ingles/atividade/atividades.html')


@login_required(login_url='/login')
def inglesAtividadesPrimeiroAno(request):
    return render(request, 'atividades/ingles/atividade/primeiroAno.html')


@login_required(login_url='/login')
def inglesAtividadesSegundoAno(request):
    return render(request, 'atividades/ingles/atividade/segundoAno.html')


@login_required(login_url='/login')
def inglesAtividadesTerceiroAno(request):
    return render(request, 'atividades/ingles/atividade/terceiroAno.html')


@login_required(login_url='/login')
def inglesAtividadesQuartoAno(request):
    return render(request, 'atividades/ingles/atividade/quartoAno.html')


@login_required(login_url='/login')
def inglesAtividadesQuintoAno(request):
    return render(request, 'atividades/ingles/atividade/quintoAno.html')


@login_required(login_url='/login')
def inglesVideos(request):
    return render(request, 'atividades/ingles/videos/videos.html')


@login_required(login_url='/login')
def inglesVideosPrimeiroAno(request):
    return render(request, 'atividades/ingles/videos/primeiroAno.html')


@login_required(login_url='/login')
def inglesVideosSegundoAno(request):
    return render(request, 'atividades/ingles/videos/segundoAno.html')


@login_required(login_url='/login')
def inglesVideosTerceiroAno(request):
    return render(request, 'atividades/ingles/videos/terceiroAno.html')


@login_required(login_url='/login')
def inglesVideosQuartoAno(request):
    return render(request, 'atividades/ingles/videos/quartoAno.html')


@login_required(login_url='/login')
def inglesVideosQuintoAno(request):
    return render(request, 'atividades/ingles/videos/quintoAno.html')
