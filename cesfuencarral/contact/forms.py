from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True,min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, min_length=3, max_length=100)
    phone = forms.CharField(label='Teléfono', required=True, min_length=3, max_length=20)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea, min_length=10, max_length=1000)

class ContactMediosForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True,min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, min_length=3, max_length=100)
    phone = forms.CharField(label='Teléfono', required=True, min_length=3, max_length=20)

    public_options = [
        ('SMR', 'SMR'),
        ('Dependencia', 'Dependencia'),
        ('Enfermería', 'Enfermería'),
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices= public_options
    )
    
class ContactSuperiorForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True,min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, min_length=3, max_length=100)
    phone = forms.CharField(label='Teléfono', required=True, min_length=3, max_length=20)

    public_options = [
        ('DAM', 'DAM'),
        ('INTEGRACIÓN', 'INTEGRACIÓN'),
        ('INFANTIL', 'INFANTIL'),
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices= public_options
    )
    