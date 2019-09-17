from django.shortcuts import render
from django.views.generic import CreateView
from .models import RespuestaPredefinida
from django.contrib.messages.views import SuccessMessageMixin
from .forms import IncluirRespuestaP, ConsultarRespuestaP, ModificarRespuestaP
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from Artemis.mixin import AuthenticatedAdminMixin

# Create your views here.

class crear_resp(AuthenticatedAdminMixin, SuccessMessageMixin, CreateView):
    model = RespuestaPredefinida
    form_class = IncluirRespuestaP
    template_name = "resp_predefinida/crear_resp.html"
    success_url = reverse_lazy('crear_resp')
    success_message = "e"

class lista_resp(AuthenticatedAdminMixin, ListView):
    model = RespuestaPredefinida
    template_name = "resp_predefinida/lista_resp.html"

    def get_context_data(self, **kwargs):
        context = super(lista_resp, self).get_context_data(**kwargs)
        context['object_list'] = RespuestaPredefinida.objects.filter(estatus='A')
        return context

class consultar_resp(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = RespuestaPredefinida
    form_class = ConsultarRespuestaP
    template_name = "resp_predefinida/consultar_resp.html"
    success_url = reverse_lazy('lista_resp')
    success_message = "e"

class modificar_resp(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = RespuestaPredefinida
    form_class = ModificarRespuestaP
    template_name = "resp_predefinida/modificar_resp.html"
    success_url = reverse_lazy('consultar_resp')
    success_message = "e"

    def get_success_url(self):
        id_cat = self.kwargs['pk']
        return reverse_lazy('consultar_resp', kwargs={'pk':id_cat})