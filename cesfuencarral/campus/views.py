from django.shortcuts import render
from django.views.generic.base import TemplateView

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
