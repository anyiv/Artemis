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

def claimlist(request):
    return render(request, 'reclamo/claimlist.html', {})

def claimfinished(request):
    return render(request, 'reclamo/claimfinished.html', {})

def claimexpire(request):
    return render(request, 'reclamo/claimexpire.html', {})

def createclaim(request):
    return render(request, 'reclamo/createclaim.html', {})

def atc_createclaim(request):
    return render(request, 'reclamo/atc_createclaim.html', {})

def checkclaim(request):
    return render(request, 'reclamo/checkclaim.html', {})

class createclaimcategory(AuthenticatedAdminMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    form_class = IncluirCategoriaForm
    template_name = "reclamo/createclaimcategory.html"
    success_url = reverse_lazy('createclaimcategory')
    success_message = "e"

def attendclaim(request):
    return render(request, 'reclamo/attendclaim.html', {})

class claimcategorylist(AuthenticatedAdminMixin, ListView):
    model = Categoria
    template_name = "reclamo/claimcategorylist.html"

    def get_context_data(self, **kwargs):
        context = super(claimcategorylist, self).get_context_data(**kwargs)
        context['object_list'] = Categoria.objects.filter(estatus='A')
        return context

class checkclaimcategory(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = ConsultarCategoriaForm
    template_name = "reclamo/checkclaimcategory.html"
    success_url = reverse_lazy('claimcategorylist')
    success_message = "e"

def finishedclaimlist(request):
    return render(request, 'reclamo/finishedclaimlist.html', {})

def satisfactionsurvey(request):
    return render(request, 'reclamo/satisfactionsurvey.html', {})

class updateclaimcategory(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = ActualizarCategoriaForm
    template_name = "reclamo/updateclaimcategory.html"
    success_message = "e"

    def get_success_url(self):
        id_cat = self.kwargs['pk']
        return reverse_lazy('checkclaimcategory', kwargs={'pk':id_cat})

class check_claimcli(AuthenticatedClienteMixin, DetailView):
    model = Reclamo
    template_name = "reclamo/check_claimcli.html"