from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Nota, Category
from .forms import NotaForm


# Create your views here.
def index(request):
    total: int = 0
    dados = get_list_or_404(Nota)

    for item in dados:
        total += item.value

    return render(request, 'nota/index.html', {'dados': dados, 'total': total})


def detail_gasto(request, pk):
    nota = get_object_or_404(Nota, pk=pk)

    return render(request, 'nota/crud/detail.html', context={'nota': nota})


def add_note(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=Nota())

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = NotaForm(instance=Nota())

    return render(request, 'nota/crud/form.html', context={'form': form, 'category': category})


def update_gasto(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    category = Category.objects.all()
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = NotaForm(instance=nota)

    return render(request, 'nota/crud/form.html', context={'form': form, 'category': category})


def delete_gasto(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    nota.delete()
    return redirect('home')

