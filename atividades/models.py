from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Jogos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    url = models.CharField(max_length=100)
    ano = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    data_utilizacao = models.DateTimeField('date published')
    materia = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='fotos')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Jogos'


class Videos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    url = models.CharField(max_length=100)
    ano = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    data_utilizacao = models.DateTimeField('date published')
    materia = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='fotos')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Videos'


class Atividades(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    url = models.CharField(max_length=100)
    ano = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    data_utilizacao = models.DateTimeField('date published')
    materia = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='fotos')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Atividades'


