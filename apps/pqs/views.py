from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import PQS
from apps.usuario.models import User
from apps.resp_predefinida.models import RespuestaPredefinida
from .forms import CrearPeticion, CrearQueja, CrearSugerencia
from Artemis.mixin import AuthenticatedClienteMixin, AuthenticatedClienteGPQSMixin, AuthenticatedAtClienteMixin, AuthenticatedGPQSAtClienteClienteMixin

#PETICION
class cli_crearpeticion(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearPeticion
    template_name = "peticion/cli_crearpeticion.html"
    success_url = reverse_lazy('cli_crearpeticion')
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

class atc_crearpeticion(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearPeticion
    template_name = "peticion/atc_crearpeticion.html"
    success_url = reverse_lazy('atc_crearpeticion')
    success_message = "e"

#QUEJA
class cli_crearqueja(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearQueja
    template_name = "queja/cli_crearqueja.html"
    success_url = reverse_lazy('cli_crearqueja')
    success_message = "e"

class atc_crearqueja(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearQueja
    template_name = "queja/atc_crearqueja.html"
    success_url = reverse_lazy('atc_crearqueja')
    success_message = "e"

#SUGERENCIA
class cli_crearsugerencia(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearSugerencia
    template_name = "sugerencia/cli_crearsugerencia.html"
    success_url = reverse_lazy('cli_crearsugerencia')
    success_message = "e"

class atc_crearsugerencia(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearSugerencia
    template_name = "sugerencia/atc_crearsugerencia.html"
    success_url = reverse_lazy('atc_crearsugerencia')
    success_message = "e"

#CONSULTAR PQS CLIENTE
class consultarpqs(AuthenticatedGPQSAtClienteClienteMixin, DetailView):
    model = PQS
    template_name= "pqs/consultarpqs.html"

#ATENDER PQS
class atenderpqs(DetailView):
    model = PQS
    template_name = "pqs/atenderpqs.html"

    def get_context_data(self, **kwargs):
        context = super(atenderpqs, self).get_context_data(**kwargs)
        pet = RespuestaPredefinida.objects.filter(categoria = 'pet', estatus = 'A' )
        que = RespuestaPredefinida.objects.filter(categoria = 'que', estatus = 'A' )
        sug = RespuestaPredefinida.objects.filter(categoria = 'sug', estatus = 'A' )
        pri = pet.union(que)
        context['resp'] = pri.union(sug)
        return context

#PQS MARCADAS
def pqsmarcados(request):
    return render(request, 'pqs/pqsmarcados.html', {})


def g_listapqs(request):
    return render(request, 'usuario/gestpqs/g_listapqs.html', {})