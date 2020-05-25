from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('becas/', views.becas, name='becas'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('instalaciones/', views.instalaciones, name='instalaciones'),
    path('legal/', views.legal, name='legal'),
]
