from django.contrib import admin
from .models import Page


"""
Esta es la configuración para que aparezca el modelo de creacióned consultas
en el panel de administración de Django

"""

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
