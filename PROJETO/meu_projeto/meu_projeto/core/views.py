from django.shortcuts import render, get_object_or_404
from .models import Estudante, Professor, Curso, Entrega

def home(request):
    return render(request, 'index.html')

def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'AppCoder/estudantes_list.html', {'estudantes': estudantes})

def detalhe_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    return render(request, 'AppCoder/estudante_detail.html', {'estudante': estudante})

