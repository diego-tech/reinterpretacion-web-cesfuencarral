from django.urls import path
from . import views

"""
urls.py es una fichero en el que se guardan los nombres de las urls del redireccionamiento
esté fichero habrá que pasarlo al urls.py principal de la carpeta principal del proyecto

"""

urlpatterns = [
    path('', views.contacto, name='contacto'),
    path('smr/', views.smr, name='smr'),
    path('dependencia/', views.dependencia, name='dependencia'),
    path("enfermeria/", views.enfermeria, name='enfermeria'),
    path('dam/', views.dam, name='dam'),
    path('integracion/', views.integracion, name='integracion'),
    path("infantil/", views.infantil, name='infantil'),
]
