from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime


class Categoria(models.Model):
    tipo = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.tipo


class Utilizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.CharField(max_length=100, default='utilizador.svg')
    credito = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def total_credito(self):
        return self.credito

    def adicionar_credito(self, value):
        if value >= 0:
            self.credito = self.credito + value
            self.save()

    def remover_credito(self, value):
        if self.credito - value >= 0 and value > 0:
            self.credito = self.credito - value
            self.save()

class Produto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    likes = models.ManyToManyField(User, related_name='likes')
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default="", related_name="Categoria")
    quantidade = models.IntegerField(default=0)
    descricao = models.TextField()  # mudar
    preco = models.FloatField(default=0) # decimal field ??
    imagem = models.CharField(max_length=100, default='produto.svg')
    #imagem = models.ImageField(upload_to='images/utilizador/')

    NOVO = 'novo'
    USADO = 'usado'
    OPCOES_CONDICAO = (
        (NOVO, 'Novo'),
        (USADO, 'Usado'),
    )
    condicao = models.CharField(choices=OPCOES_CONDICAO, default=NOVO, max_length=100)

    def total_likes(self):
        return self.likes.count()


class Rating(models.Model):
    None
    # https://django-star-ratings.readthedocs.io/en/latest/
    # Checkem isto e digam se gostam ou nao
    # ter uma coisa logo completa seria muito bom, só não percebi muito bem como funciona.


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    texto = models.TextField()


# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
#     produto = models.ForeignKey(Produto, on_delete=models.CASCADE, primary_key=True)
