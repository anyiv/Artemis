from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import IncluirCategoriaForm, ConsultarCategoriaForm, ActualizarCategoriaForm
from .models import Categoria, Reclamo
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from Artemis.mixin import AuthenticatedAdminMixin, AuthenticatedClienteMixin

# Create your views here.

def g_listareclamos(request):
    return render(request, 'reclamo/g_listareclamos.html', {})

def g_reclamosfinalizados(request):
    return render(request, 'reclamo/g_reclamosfinalizados.html', {})

def reclamosporvencer(request):
    return render(request, 'reclamo/reclamosporvencer.html', {})

def cli_crearReclamo(request):
    return render(request, 'reclamo/cli_crearReclamo.html', {})

def atc_crearReclamo(request):
    return render(request, 'reclamo/atc_crearReclamo.html', {})

def gt_consultarReclamo(request):
    return render(request, 'reclamo/gt_consultarReclamo.html', {})

class crearcatreclamo(AuthenticatedAdminMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    form_class = IncluirCategoriaForm
    template_name = "categoria_reclamo/crearcatreclamo.html"
    success_url = reverse_lazy('crearcatreclamo')
    success_message = "e"

def atenderReclamo(request):
    return render(request, 'reclamo/atenderReclamo.html', {})

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

def cli_reclamosfinalizados(request):
    return render(request, 'reclamo/cli_reclamosfinalizados.html', {})

def encuesta_cliente(request):
    return render(request, 'reclamo/encuesta_cliente.html', {})

class modificarcatreclamo(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = ActualizarCategoriaForm
    template_name = "categoria_reclamo/modificarcatreclamo.html"
    success_message = "e"

    def get_success_url(self):
        id_cat = self.kwargs['pk']
        return reverse_lazy('consultarcatreclamo', kwargs={'pk':id_cat})

class cli_consultarReclamo(AuthenticatedClienteMixin, DetailView):
    model = Reclamo
    template_name = "reclamo/cli_consultarReclamo.html"