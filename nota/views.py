from django.shortcuts import render
from .models import Nota, Category


# Create your views here.
def index(request):
    dados = Nota.objects.all()

    return render(request, 'nota/index.html', {'dados': dados})
