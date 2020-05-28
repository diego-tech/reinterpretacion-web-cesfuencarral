from django import forms
from .models import Page



"""
Formulario de creación de las consultas

"""
class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Alumno y Grado'}),   
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Título'})
        }

        labels = {
            'title':'',
            'subtitle':'',
            'order':'',
            'content':'',
        }