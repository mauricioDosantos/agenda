from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=90)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_criacao = models.DateField(default=timezone.now)
    descricao = models.CharField(max_length=400)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome