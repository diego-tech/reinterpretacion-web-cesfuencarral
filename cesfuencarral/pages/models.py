from django.db import models
from ckeditor.fields import RichTextField


"""
Este modelo es el modelo de creación de consultas con el editor ckeditor.

"""

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    subtitle = models.CharField(verbose_name='Nombre Alumno y Grado', max_length=500)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['-created']

    def __str__(self):
        return self.title
