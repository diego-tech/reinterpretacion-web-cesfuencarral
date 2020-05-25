from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Imagenes(models.Model):
    title = models.CharField(max_length=200,verbose_name='Título')
    slider1 = models.ImageField(verbose_name='slider1', upload_to='images', null=True, blank=True)
    slider2 = models.ImageField(verbose_name='slider2', upload_to='images', null=True, blank=True)
    slider3 = models.ImageField(verbose_name='slider3', upload_to='images', null=True, blank=True)
    slider4 = models.ImageField(verbose_name='slider4', upload_to='images', null=True, blank=True)
    smr = models.ImageField(verbose_name='SMR', upload_to='images', null=True, blank=True)
    dependencia = models.ImageField(verbose_name='DEPENDENCIA', upload_to='images', null=True, blank=True)
    enfermeria = models.ImageField(verbose_name='ENFERMERÍA', upload_to='images', null=True, blank=True)
    dam = models.ImageField(verbose_name='DAM', upload_to='images', null=True, blank=True)
    integracion = models.ImageField(verbose_name='INTEGRACIÓN', upload_to='images', null=True, blank=True)
    infantil = models.ImageField(verbose_name='INFANTIL', upload_to='images', null=True, blank=True)
    new1 = models.ImageField(verbose_name='new1', upload_to='images', null=True, blank=True)
    new2 = models.ImageField(verbose_name='new2', upload_to='images', null=True, blank=True)
    new3 = models.ImageField(verbose_name='new3', upload_to='images', null=True, blank=True)
    new4 = models.ImageField(verbose_name='new4', upload_to='images', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'imágen'
        verbose_name_plural = 'imágenes'
        ordering = ['-created']

    def __str__(self):
        return self.title
