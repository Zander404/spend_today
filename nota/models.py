from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Nota(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, help_text='Titulo para a compra feita')
    description = models.TextField(max_length=255, blank=True, null=True, help_text='Descrição do que foi comprado')
    value = models.FloatField(blank=True, null=True, help_text='Valor da Compra')
    datetime = models.DateField(blank=True, null=True, help_text='Dia em que a comprar foi efetuada')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='Categoria da Comprar feita')

    def __str__(self):
        return self.name
