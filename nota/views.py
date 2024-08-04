from django.shortcuts import render
from .models import Nota, Category


# Create your views here.
def index(request):
    total: int = 0
    dados = Nota.objects.all()

    for item in dados:
        total += item.value

    return render(request, 'nota/index.html', {'dados': dados, 'total': total})
