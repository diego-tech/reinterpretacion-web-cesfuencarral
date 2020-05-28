from django.shortcuts import render
from django.views.generic.base import TemplateView

"""
Para todo el campus virtual usaremos vistas basadasen clases por que para 
estos casos son mejores ya que implementan más funcionalidades que haciendolas con vistas
basadas en funciones sería más engorroso

https://ccbv.co.uk/

"""

# Create your views here.
class CampusPageView(TemplateView):
    template_name = 'campus/home.html'

class SamplePageView(TemplateView):
    template_name = 'campus/sample.html'

def index(request):
    if request.user.is_authenticated():
        print("Logged in")
    else:
        print("Not logged in")
