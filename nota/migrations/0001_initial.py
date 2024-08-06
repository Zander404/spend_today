# Generated by Django 5.0.7 on 2024-08-06 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Titulo para a compra feita', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Descrição do que foi comprado', max_length=255)),
                ('value', models.DecimalField(blank=True, decimal_places=2, help_text='Valor da Compra', max_digits=10)),
                ('datetime', models.DateField(blank=True, help_text='Dia em que a comprar foi efetuada')),
                ('category', models.ForeignKey(help_text='Categoria da Comprar feita', on_delete=django.db.models.deletion.CASCADE, to='nota.category')),
            ],
        ),
    ]
