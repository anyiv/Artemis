from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import PQS, HistoricoPQS
from django.http import HttpResponseRedirect
from apps.usuario.models import User
from apps.resp_predefinida.models import RespuestaPredefinida
from .forms import CrearPeticion, CrearQueja, CrearSugerencia, AtenderPQS
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
        hpqs = HistoricoPQS()
        hpqs.detalle = "La petición se ha creado."
        hpqs.pqs = self.object
        hpqs.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nueva petición registrada con éxito',
            'Gracias por comunicarnos tu petición.',
            'Es muy útil escuchar las peticiones como la tuya.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())

class atc_crearpeticion(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearPeticion
    template_name = "peticion/atc_crearpeticion.html"
    success_url = reverse_lazy('atc_crearpeticion')
    success_message = "e"

    def form_valid(self, form):
        self.object = form.save()
        hpqs = HistoricoPQS()
        hpqs.detalle = "La petición se ha sido creada."
        hpqs.pqs = self.object
        hpqs.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nueva petición registrada con éxito',
            'Gracias por comunicarnos tu petición.',
            'Es muy útil escuchar las peticiones como la tuya.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())

#QUEJA
class cli_crearqueja(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearQueja
    template_name = "queja/cli_crearqueja.html"
    success_url = reverse_lazy('cli_crearqueja')
    success_message = "e"

    def form_valid(self, form):
        self.object = form.save()
        hpqs = HistoricoPQS()
        hpqs.detalle = "La queja se ha sido creada."
        hpqs.pqs = self.object
        hpqs.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nueva queja registrada con éxito',
            'Gracias por comunicarnos tu queja.',
            'Es muy útil para nosotros saber tus opiniones.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())


class atc_crearqueja(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearQueja
    template_name = "queja/atc_crearqueja.html"
    success_url = reverse_lazy('atc_crearqueja')
    success_message = "e"

    def form_valid(self, form):
        self.object = form.save()
        hpqs = HistoricoPQS()
        hpqs.detalle = "La queja se ha sido creada."
        hpqs.pqs = self.object
        hpqs.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nueva queja registrada con éxito',
            'Gracias por comunicarnos tu queja.',
            'Es muy útil para nosotros saber tus opiniones.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())

#SUGERENCIA
class cli_crearsugerencia(AuthenticatedClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearSugerencia
    template_name = "sugerencia/cli_crearsugerencia.html"
    success_url = reverse_lazy('cli_crearsugerencia')
    success_message = "e"

    def form_valid(self, form):
        self.object = form.save()
        hpqs = HistoricoPQS()
        hpqs.detalle = "La sugerencia se ha sido creada."
        hpqs.pqs = self.object
        hpqs.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nueva sugerencia registrada con éxito',
            'Gracias por comunicarnos tu sugerencia.',
            'Es muy útil para nosotros saber las sugerencias que tienes para mejorar nuestra organización.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())

class atc_crearsugerencia(AuthenticatedAtClienteMixin, SuccessMessageMixin, CreateView):
    model = PQS
    form_class = CrearSugerencia
    template_name = "sugerencia/atc_crearsugerencia.html"
    success_url = reverse_lazy('atc_crearsugerencia')
    success_message = "e"

    def form_valid(self, form):
        self.object = form.save()
        hpqs = HistoricoPQS()
        hpqs.detalle = "La sugerencia se ha sido creada."
        hpqs.pqs = self.object
        hpqs.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nueva sugerencia registrada con éxito',
            'Gracias por comunicarnos tu sugerencia.',
            'Es muy útil para nosotros saber las sugerencias que tienes para mejorar nuestra organización.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())

#CONSULTAR PQS CLIENTE
class consultarpqs(AuthenticatedGPQSAtClienteClienteMixin, DetailView):
    model = PQS
    template_name= "pqs/consultarpqs.html"

    def get_context_data(self, **kwargs):
        context = super(consultarpqs, self).get_context_data(**kwargs)
        context["hist"] = HistoricoPQS.objects.filter(pqs=self.kwargs['pk'])
        return context
    

#ATENDER PQS
class atenderpqs(UpdateView):
    model = PQS
    form_class = AtenderPQS
    template_name = "pqs/atenderpqs.html"

    def form_valid(self, form):
        pqs_vjo = PQS.objects.get(codPQS=self.kwargs['pk'])
        pqs_nvo = form.save()
        pqs_nvo.responsablePQS.add(self.request.user)
        if pqs_nvo.estatus == 'M' and pqs_vjo.estatus == 'P':
            hpqs = HistoricoPQS()
            hpqs.detalle= "La " + pqs_vjo.get_categoria_display() + " ha cambiado de estatus a Marcada."
            hpqs.usuarioEncargado = self.request.user
            hpqs.pqs = pqs_vjo
            hpqs.save()
        pqs_nvo.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(atenderpqs, self).get_context_data(**kwargs)
        rp = RespuestaPredefinida.objects.filter(estatus = 'A')
        pet = rp.filter(categoria = 'pet')
        que = rp.filter(categoria = 'que' )
        sug = rp.filter(categoria = 'sug')
        pri = pet.union(que)
        context['resp'] = pri.union(sug)
        return context

    def get_success_url(self):
        idpqs=self.kwargs['pk']
        messages.add_message(self.request, messages.INFO, 'e')
        return reverse_lazy('consultarpqs', kwargs={'pk': idpqs})

#PQS MARCADAS
class reporte_pqsmarcados(ListView):
    model = PQS
    template_name = "pqs/reporte_pqsmarcados.html"

    def get_context_data(self, **kwargs):
        context = super(reporte_pqsmarcados, self).get_context_data(**kwargs)
        context['pqsmar'] = PQS.objects.filter(estatus = 'M')
        return context

class pqsmarcados(ListView):
    model = PQS
    template_name = "pqs/pqsmarcados.html"

    def get_context_data(self, **kwargs):
        context = super(pqsmarcados, self).get_context_data(**kwargs)
        context['pqsmar'] = PQS.objects.filter(estatus = 'M')
        return context

class g_listapqs(ListView):
    model = PQS
    template_name = "pqs/g_listapqs.html"

    def get_context_data(self, **kwargs):
        context = super(g_listapqs, self).get_context_data(**kwargs)
        context['pqs_pen'] = PQS.objects.filter(estatus='P')
        return context