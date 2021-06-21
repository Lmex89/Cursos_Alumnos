from django.shortcuts import render
from Clases.models import Alumnos, Clases
# Create your views here.


def Alumnos_view(request):
    alumnos = Alumnos.objects.all()
    context = {'alumnos': alumnos}
    return render(request,
                  'alumnos/Alumnos_view.html',
                  context)


def get_alumno(request, pk):
    try:
        alumno = Alumnos.objects.get(pk=pk)
        context = {'alumno': alumno}
        return render(request,
                      'alumnos/alumnos_detalle.html',
                      context)
    except Exception as error:
        context = {'alumno': ""}
        return render(request, 'alumnos/alumnos_detalle.html',
                      context)


def get_clases_view(request):
    cursos = Clases.objects.all()
    context = {'cursos': cursos}
    return render(request,
                  'alumnos/cursos_view.html',
                  context)


def get_clases_detalle(request, pk):
    try:
        curso = Clases.objects.get(pk=pk)
        alumnos_class = curso.alumnos.all()
        print(alumnos_class)
        context = {'curso': curso,
                   'alumnos': alumnos_class,
                   'path': '/alumnos/'}
        return render(request,
                      'alumnos/cursos_detalle.html',
                      context)
    except Exception as error:
        print(str(error))
        context = {'curso': ""}
        return render(request, 'alumnos/cursos_detalle.html',
                      context)
