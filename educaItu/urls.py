"""educaItu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from atividades.views import home, sign_in, sair, submit_login, portugues, matematica, historia, geografia, ciencias, ingles, jogos, videos, atividades


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('login/', sign_in),
    path('logout/', sair),
    path('login/submit', submit_login),
    path('portugues/', portugues), 
    path('matematica/', matematica), 
    path('historia/', historia), 
    path('geografia/', geografia), 
    path('ciencias/', ciencias), 
    path('ingles/', ingles), 
    path('jogos/', jogos), 
    path('videos/', videos), 
    path('atividades/', atividades), 
]
