from django.contrib import admin
from .models import Noticias

# Register your models here.

"""
En el admin.py se registan los modelos para que se vean en el panel de administrador de Django

"""


class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Noticias, NoticiasAdmin)