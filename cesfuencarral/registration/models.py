from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

"""
En este models.py tenemos dos configuraciones diferentes,
la configuración típica de cualquier modelo que queramos implementar, en este caso
el modelo de el formulario de creación de un perfil y dos configuraciones más.


La configuración custom_upload_to es una configuración de los avatares de los usuarios,
cuando el usuario elimina el antiguo avatar y sube otro, automáticamente el anterior se elimina de la base de datos
y se sube el nuevo avatar.

Y la configuración ensure_profile_exists es una configuración para que todos los nuevos usuarios registrados,
cuenten automáticamente con un perfil visible aunque no haya sido configurado por el usuario, es decir, si yo creo el User1 este usuario
automáticamente tendrá un perfil con una descripción vacía y con un avatar fijo visible.

"""

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)


    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")