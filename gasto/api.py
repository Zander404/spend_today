from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes


from gasto.models import Pessoa, Gasto, Categoria
from gasto.serializers import Pessoa_Serializer, Gasto_Serializer, Categoria_Serializer


@api_view(['GET'])
def pessoa(request):
    pessoa = Pessoa.objects.all()
    pessoa_serializer = Pessoa_Serializer(pessoa, many=True)
    return JsonResponse(pessoa_serializer.data, safe=False)


@api_view(['GET'])
def gasto(request):
    gasto = Gasto.objects.all()
    gasto_serializer = Gasto_Serializer(gasto, many=True)
    return JsonResponse(gasto_serializer.data, safe=False)


def categoria(request):
    categoria = Categoria.objects.all()
    categoria_serializer = Categoria_Serializer(categoria, many=True)
    return JsonResponse(categoria_serializer.data, safe=False)
