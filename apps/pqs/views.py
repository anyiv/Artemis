from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import PQS
from apps.usuario.models import User
from .forms import CrearPeticion, CrearQueja, CrearSugerencia
from Artemis.mixin import AuthenticatedClienteMixin, AuthenticatedClienteGPQSMixin, AuthenticatedAtClienteMixin

#PETICION
class createpetition(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearPeticion
    template_name = "peticion/createpetition.html"
    success_url = reverse_lazy('createpetition')
    success_message = "e"

    def form_valid(self, form):
        self.object = form.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nueva petición registrada con éxito',
            'Gracias por comunicarnos tu petición.',
            'Es muy útil escuchar las peticiones como la tuya.',
            'Tu mensaje: ' + self.object.descripcion, 
            self.object.nombreUsuario.idCliente.nombre + ' ' + self.object.nombreUsuario.idCliente.apellido
        )
        return redirect(self.get_success_url())
        
def checkpetition(request):
    return render(request, 'peticion/checkpetition.html', {})

class atc_createpetition(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearPeticion
    template_name = "peticion/atc_createpetition.html"
    success_url = reverse_lazy('atc_createpetition')
    success_message = "e"

#QUEJA
class createcomplaint(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearQueja
    template_name = "queja/createcomplaint.html"
    success_url = reverse_lazy('createcomplaint')
    success_message = "e"

class atc_createcomplaint(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearQueja
    template_name = "queja/atc_createcomplaint.html"
    success_url = reverse_lazy('atc_createcomplaint')
    success_message = "e"

#SUGERENCIA
class createsuggestion(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearSugerencia
    template_name = "sugerencia/createsuggestion.html"
    success_url = reverse_lazy('createsuggestion')
    success_message = "e"

class atc_createsuggestion(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearSugerencia
    template_name = "sugerencia/atc_createsuggestion.html"
    success_url = reverse_lazy('atc_createsuggestion')
    success_message = "e"

#CONSULTAR PQS CLIENTE
class check_pqs(AuthenticatedClienteGPQSMixin, DetailView):
    model = PQS
    template_name= "pqs/check_pqs.html"


#ATENDER PQS
class attendpqs(DetailView):
    model = PQS
    template_name = "pqs/attendpqs.html"

#PQS MARCADAS

def pqsmarked(request):
    return render(request, 'pqs/pqsmarked.html', {})