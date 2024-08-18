from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()


class Categoria(models.Model):
    name = models.CharField(max_length=100)
    


class Gasto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    fk_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)



