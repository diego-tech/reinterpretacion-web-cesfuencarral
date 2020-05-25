from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name='contacto'),
    path('smr/', views.smr, name='smr'),
    path('dependencia/', views.dependencia, name='dependencia'),
    path("enfermeria/", views.enfermeria, name='enfermeria'),
    path('dam/', views.dam, name='dam'),
    path('integracion/', views.integracion, name='integracion'),
    path("infantil/", views.infantil, name='infantil'),
]
