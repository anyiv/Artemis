from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import PQS
from .forms import CrearPeticion, CrearQueja, CrearSugerencia

# Create your views here.

#PETICION
class createpetition(SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearPeticion
    template_name = "peticion/createpetition.html"
    success_url = reverse_lazy ('createpetition')
    success_message = "e"

    
def checkpetition(request):
    return render(request, 'peticion/checkpetition.html', {})


def atc_createpetition(request):
    return render(request, 'peticion/atc_createpetition.html', {})

#QUEJA
class createcomplaint(SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearQueja
    template_name = "queja/createcomplaint.html"
    success_url = reverse_lazy('createcomplaint')
    success_message = "e"

def atc_createcomplaint(request):
    return render(request, 'queja/atc_createcomplaint.html', {})


#SUGERENCIA
class createsuggestion(SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearSugerencia
    template_name = "sugerencia/createsuggestion.html"
    success_url = reverse_lazy('createsuggestion')
    success_message = "e"

def atc_createsuggestion(request):
    return render(request, 'sugerencia/atc_createsuggestion.html', {})