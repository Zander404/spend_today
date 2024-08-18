from rest_framework import serializers
from .models import Pessoa, Categoria, Gasto


class Pessoa_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'



class Categoria_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'



class Gasto_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'