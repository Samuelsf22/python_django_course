from django.shortcuts import render
from .models import Lista_curso

# Create your views here.


def lista_cursos(request):
    cursos = Lista_curso.objects.values()
    return render(request, 'cursostm/cursos.html', {
        'cursos': cursos
    })


def lista_cursos_2024(request):
    cursos = Lista_curso.objects.values()
    return render(request, 'cursostm/cursos_2024.html', {
        'cursos': cursos
    })
