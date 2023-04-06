from django.shortcuts import render
from .models import curso
from django.http import HttpResponse

# Create your views here.


def crear_curso(request):
    
    nombre_curso="python"
    comision_curso="51325"

    curso1=curso(nombre = nombre_curso, comision = comision_curso)
    curso1.save()

    respuesta =f"Curso creado --- {nombre_curso} -- {comision_curso}"
    
    return HttpResponse(respuesta)

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def inicio(request):
    return HttpResponse ("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")