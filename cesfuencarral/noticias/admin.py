from django.contrib import admin
from .models import Noticias

# Register your models here.
class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Noticias, NoticiasAdmin)