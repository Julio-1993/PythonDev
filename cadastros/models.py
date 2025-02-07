from django.db import models

# Create your models here.
class NomeResponsavel (models.Model):
    nome = models.CharField(max_length=30,blank=False, null=False)
    sobrenome = models.CharField(max_length=30,blank=False, null=False)

    def __str__(self):
        return self.nome

class Animal (models.Model):
    CIIC = models.CharField(max_length=11, blank=False, null=False)
    Nome = models.CharField(max_length=30, blank=False, null=False)

class Cadastrodeficha (models.Model):
    ficha = models.CharField(max_length=500, blank=False, null=False)
