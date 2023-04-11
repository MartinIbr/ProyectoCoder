from django.shortcuts import render
from .models import curso, profesor
from .forms import ProfesorForm
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
    
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            Profesor = profesor()
            Profesor.nombre = form.cleaned_data['nombre']
            Profesor.apellido = form.cleaned_data['apellido']
            Profesor.email = form.cleaned_data['email']
            Profesor.profesion = form.cleaned_data['profesion']
            Profesor.save()
            form = ProfesorForm()
    else:
        form = ProfesorForm()


    profesores = profesor.objects.all()
    context = {"profesores": profesores, "form" : form}
    return render(request, "AppCoder/profesores.html", context)

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def inicio(request):
    return HttpResponse ("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")