from django.urls import path
from . import views

"""
urls.py es una fichero en el que se guardan los nombres de las urls del redireccionamiento
esté fichero habrá que pasarlo al urls.py principal de la carpeta principal del proyecto

"""

urlpatterns = [
    path('', views.home, name='home'),
    path('becas/', views.becas, name='becas'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('instalaciones/', views.instalaciones, name='instalaciones'),
    path('legal/', views.legal, name='legal'),
]
