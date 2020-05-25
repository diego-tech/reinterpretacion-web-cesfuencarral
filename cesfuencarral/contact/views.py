from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm, ContactMediosForm, ContactSuperiorForm

# Create your views here.

#Contacto general
def contacto(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            content = request.POST.get('content', '')
            # Enviar el correo y redireccionamos
            email = EmailMessage(
                'Ces Fuencarral: Nuevo Mensaje de Contacto',
                'De {} Con Email <{}> y Número {} \n\nEscribío:\n\n{}'.format(name, email, phone ,content),
                'no-contestar@ibox.mailtrap.io',
                ['dieguitoprogramacion@gmail.com'],
                reply_to=[email]
            )

            try:
                email.send()
                # Todo ha ideo bien,redireccionamos a OK
                return redirect(reverse('contacto')+'?ok')
            except:
                #Algo no ha ido bien redireccionamos a FAIL
                return redirect(reverse('contacto')+'?fail')

    return render(request, 'contact/contacto.html', {'form':contact_form})

#Contacto Grados Medios
def smr(request):
    contact_forms_medio = ContactMediosForm(data=request.POST)

    if contact_forms_medio.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        public = request.POST.get('public', '')
        phone = request.POST.get('phone', '')
        # Enviamos el correo y redireccionamos
        email = EmailMessage(
            'Ces Fuencarral: Nuevo mensaje de {}'.format(public),
            'De {} Con Email:{} Y teléfono {} solicita información sobre {}'.format(name, email, phone, public),
            'no-contestar@inbox.mailtrap.io',
            ['dieguitoprogramacion@gmail.com'],
            reply_to=[email]
        )
        
        try:
            email.send()
            # Todo ha ido bien, redireccionamos a OK
            return redirect(reverse('smr')+'?ok')
        except:
            # Algo no ha ido bien, redireccionamos a Fail
            return redirect(reverse('smr')+'?fail')

    return render(request, 'contact/smr.html', {'form':contact_forms_medio})

def dependencia(request):
    contact_forms_medio = ContactMediosForm(data=request.POST)

    if contact_forms_medio.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        public = request.POST.get('public', '')
        phone = request.POST.get('phone', '')
        # Enviamos el correo y redireccionamos
        email = EmailMessage(
            'Ces Fuencarral: Nuevo mensaje de {}'.format(public),
            'De {} Con Email:{} Y teléfono {} solicita información sobre {}'.format(name, email, phone, public),
            'no-contestar@inbox.mailtrap.io',
            ['dieguitoprogramacion@gmail.com'],
            reply_to=[email]
        )
        
        try:
            email.send()
            # Todo ha ido bien, redireccionamos a OK
            return redirect(reverse('smr')+'?ok')
        except:
            # Algo no ha ido bien, redireccionamos a Fail
            return redirect(reverse('smr')+'?fail')

    return render(request, 'contact/dependencia.html', {'form':contact_forms_medio})

def enfermeria(request):
    contact_forms_medio = ContactMediosForm(data=request.POST)

    if contact_forms_medio.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        public = request.POST.get('public', '')
        phone = request.POST.get('phone', '')
        # Enviamos el correo y redireccionamos
        email = EmailMessage(
            'Ces Fuencarral: Nuevo mensaje de {}'.format(public),
            'De {} Con Email:{} Y teléfono {} solicita información sobre {}'.format(name, email, phone, public),
            'no-contestar@inbox.mailtrap.io',
            ['dieguitoprogramacion@gmail.com'],
            reply_to=[email]
        )
        
        try:
            email.send()
            # Todo ha ido bien, redireccionamos a OK
            return redirect(reverse('smr')+'?ok')
        except:
            # Algo no ha ido bien, redireccionamos a Fail
            return redirect(reverse('smr')+'?fail')

    return render(request, 'contact/enfermeria.html', {'form':contact_forms_medio})

#Contacto Grados Superiores
def dam(request):
    contact_forms_superior = ContactSuperiorForm(data=request.POST)

    if contact_forms_superior.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        public = request.POST.get('public', '')
        phone = request.POST.get('phone', '')

        # Enviamos el correo y redireccionamos
        email = EmailMessage(
            'Ces Fuencarral: Nuevo mensaje de {}'.format(public),
            'De {} Con Email:{} Y teléfono {} solicita información sobre {}'.format(name, email, phone, public),
            'no-contestar@inbox.mailtrap.io',
            ['dieguitoprogramacion@gmail.com'],
            reply_to=[email]
        )
        
        try:
            email.send()
            # Todo ha ido bien, redireccionamos a OK
            return redirect(reverse('smr')+'?ok')
        except:
            # Algo no ha ido bien, redireccionamos a Fail
            return redirect(reverse('smr')+'?fail')

    return render(request, 'contact/dam.html', {'form':contact_forms_superior})

def integracion(request):
    contact_forms_superior = ContactSuperiorForm(data=request.POST)

    if contact_forms_superior.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        public = request.POST.get('public', '')
        phone = request.POST.get('phone', '')

        # Enviamos el correo y redireccionamos
        email = EmailMessage(
            'Ces Fuencarral: Nuevo mensaje de {}'.format(public),
            'De {} Con Email:{} Y teléfono {} solicita información sobre {}'.format(name, email, phone, public),
            'no-contestar@inbox.mailtrap.io',
            ['dieguitoprogramacion@gmail.com'],
            reply_to=[email]
        )
        
        try:
            email.send()
            # Todo ha ido bien, redireccionamos a OK
            return redirect(reverse('smr')+'?ok')
        except:
            # Algo no ha ido bien, redireccionamos a Fail
            return redirect(reverse('smr')+'?fail')

    return render(request, 'contact/integracion.html', {'form':contact_forms_superior})

def infantil(request):
    contact_forms_superior = ContactSuperiorForm(data=request.POST)

    if contact_forms_superior.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        public = request.POST.get('public', '')
        phone = request.POST.get('phone', '')

        # Enviamos el correo y redireccionamos
        email = EmailMessage(
            'Ces Fuencarral: Nuevo mensaje de {}'.format(public),
            'De {} Con Email:{} Y teléfono {} solicita información sobre {}'.format(name, email, phone, public),
            'no-contestar@inbox.mailtrap.io',
            ['dieguitoprogramacion@gmail.com'],
            reply_to=[email]
        )
        
        try:
            email.send()
            # Todo ha ido bien, redireccionamos a OK
            return redirect(reverse('smr')+'?ok')
        except:
            # Algo no ha ido bien, redireccionamos a Fail
            return redirect(reverse('smr')+'?fail')

    return render(request, 'contact/infantil.html', {'form':contact_forms_superior})