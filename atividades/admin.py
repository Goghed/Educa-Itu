from django.contrib import admin
from .models import Jogos, Videos, Atividades

# Register your models here.


@admin.register(Jogos)
class Jogos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'url', 'ano', 'user', 'data', 'data_utilizacao', 'materia', 'foto', 'ativo')


@admin.register(Videos)
class Videos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'url', 'ano', 'user', 'data', 'data_utilizacao', 'materia', 'foto', 'ativo')


@admin.register(Atividades)
class Atividades(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'url', 'ano', 'user', 'data', 'data_utilizacao', 'materia', 'foto', 'ativo')



