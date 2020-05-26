from django.shortcuts import render
from . import views
from .models import Noticias
from django.core.paginator import Paginator

"""
En este archivo views.py aparte de configurar las vistas tambien configuraremos
el paginador de las páginas

"""


# Create your views here.
def noticias(request):
    noticias = Noticias.objects.all()

    paginator = Paginator(noticias, 2)
    page = request.GET.get('page')
    noticias = paginator.get_page(page)

    return render(request, 'noticias/noticias.html', {'noticias': noticias})