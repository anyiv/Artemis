from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import IncluirCategoriaForm, ConsultarCategoriaForm, ActualizarCategoriaForm, IncluirReclamo, AtenderReclamo
from .models import Categoria, Reclamo
from apps.usuario.models import User
from apps.resp_predefinida.models import RespuestaPredefinida
from apps.datos_externos.models import Contrato, DetalleContrato, Cliente, Servicio
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from Artemis.mixin import AuthenticatedAdminMixin, AuthenticatedClienteMixin, AuthenticatedGPQSAtClienteClienteMixin

# Create your views here.

#RECLAMO
class g_listareclamos(ListView):
    model = Reclamo
    template_name = "reclamo/g_listareclamos.html"

class g_reclamosfinalizados(ListView):
    model = Reclamo
    template_name = "reclamo/g_reclamosfinalizados.html"

    def get_context_data(self, **kwargs):
        context = super(g_reclamosfinalizados, self).get_context_data(**kwargs)
        context['object_list'] = Reclamo.objects.filter(estatus='F')
        return context

def reclamosporvencer(request):
    return render(request, 'reclamo/reclamosporvencer.html', {})

class cli_crearReclamo(SuccessMessageMixin, CreateView):
    model = Reclamo
    form_class = IncluirReclamo
    template_name = "reclamo/cli_crearReclamo.html"
    success_url = reverse_lazy('cli_crearReclamo')
    success_message = "e"

    def get_context_data(self, **kwargs):
        context = super(cli_crearReclamo, self).get_context_data(**kwargs)
        cliente = self.request.user.idCliente
        contrato = Contrato.objects.get(codCliente = cliente)
        detcon = DetalleContrato.objects.filter(nroContrato = contrato)
        context['serv'] = detcon
        context['catreclamo'] = Categoria.objects.filter(estatus='A')
        return context

class atc_crearReclamo(SuccessMessageMixin, CreateView):
    model = Reclamo
    template_name = "reclamo/atc_crearReclamo.html"
    form_class = IncluirReclamo
    success_url = reverse_lazy('atc_crearReclamo')
    success_message = "e"

    def get_context_data(self, **kwargs):
        context = super(atc_crearReclamo, self).get_context_data(**kwargs)
        context['catreclamo'] = Categoria.objects.filter(estatus='A')
        return context

class gt_consultarReclamo(DetailView):
    model = Reclamo
    template_name = "reclamo/gt_consultarReclamo.html"

    def get_context_data(self, **kwargs):
        context = super(gt_consultarReclamo, self).get_context_data(**kwargs)
        context['user_cliente'] = User.objects.get(idCliente=context['reclamo'].codDetContrato.nroContrato.codCliente.identificacion)
        return context
    

class atenderReclamo(SuccessMessageMixin, DetailView):
    model = Reclamo
    template_name= "reclamo/atenderReclamo.html"
    form_class = AtenderReclamo
    success_url = reverse_lazy('gt_consultarReclamo')
    success_message = "e"

    def get_context_data(self, **kwargs):
        context = super(atenderReclamo, self).get_context_data(**kwargs)
        context['rp'] = RespuestaPredefinida.objects.filter(categoria='rec',estatus='A')
        return context

def cli_reclamosfinalizados(request):
    return render(request, 'reclamo/cli_reclamosfinalizados.html', {})

def encuesta_cliente(request):
    return render(request, 'reclamo/encuesta_cliente.html', {})

class cli_consultarReclamo(AuthenticatedGPQSAtClienteClienteMixin, DetailView):
    model = Reclamo
    template_name = "reclamo/cli_consultarReclamo.html"

#CATEGORIA DE RECLAMOS
class crearcatreclamo(AuthenticatedAdminMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    form_class = IncluirCategoriaForm
    template_name = "categoria_reclamo/crearcatreclamo.html"
    success_url = reverse_lazy('crearcatreclamo')
    success_message = "e"

class listacatreclamo(AuthenticatedAdminMixin, ListView):
    model = Categoria
    template_name = "categoria_reclamo/listacatreclamo.html"

    def get_context_data(self, **kwargs):
        context = super(listacatreclamo, self).get_context_data(**kwargs)
        context['object_list'] = Categoria.objects.filter(estatus='A')
        return context

class consultarcatreclamo(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = ConsultarCategoriaForm
    template_name = "categoria_reclamo/consultarcatreclamo.html"
    success_url = reverse_lazy('listacatreclamo')
    success_message = "e"

class modificarcatreclamo(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = ActualizarCategoriaForm
    template_name = "categoria_reclamo/modificarcatreclamo.html"
    success_message = "e"

    def get_success_url(self):
        id_cat = self.kwargs['pk']
        return reverse_lazy('consultarcatreclamo', kwargs={'pk':id_cat})
