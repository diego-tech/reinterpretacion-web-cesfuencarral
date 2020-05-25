from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Noticias(models.Model):
    title = models.CharField(max_length=200,verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title

