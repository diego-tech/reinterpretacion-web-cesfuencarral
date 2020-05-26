from django.shortcuts import render
from .models import Imagenes
# Create your views here.

""" 
Estas son las vistas principales de la página web, estan basadas en funciones
estas vistas se pasan al urls.py para el redireccionamiento

"""

def home(request):
    imagenes = Imagenes.objects.all()

    return render(request, 'core/home.html', {'imagenes':imagenes})
    
def becas(request):
    return render(request, 'core/becas.html')
    
def proyectos(request):
    return render(request, 'core/proyectos.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def instalaciones(request):
    return render(request, 'core/instalaciones.html')

def legal(request):
    return render(request, 'core/aviso_legal.html')