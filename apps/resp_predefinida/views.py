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

class createpredanswer(AuthenticatedAdminMixin, SuccessMessageMixin, CreateView):
    model = RespuestaPredefinida
    form_class = IncluirRespuestaP
    template_name = "resp_predefinida/createpredanswer.html"
    success_url = reverse_lazy('createpredanswer')
    success_message = "e"

class predanswerlist(AuthenticatedAdminMixin, ListView):
    model = RespuestaPredefinida
    template_name = "resp_predefinida/predanswerlist.html"

    def get_context_data(self, **kwargs):
        context = super(predanswerlist, self).get_context_data(**kwargs)
        context['object_list'] = RespuestaPredefinida.objects.filter(estatus='A')
        return context

class checkpredanswer(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = RespuestaPredefinida
    form_class = ConsultarRespuestaP
    template_name = "resp_predefinida/checkpredanswer.html"
    success_url = reverse_lazy('predanswerlist')
    success_message = "e"

class updatepredanswer(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = RespuestaPredefinida
    form_class = ModificarRespuestaP
    template_name = "resp_predefinida/updatepredanswer.html"
    success_url = reverse_lazy('checkpredanswer')
    success_message = "e"

    def get_success_url(self):
        id_cat = self.kwargs['pk']
        return reverse_lazy('checkpredanswer', kwargs={'pk':id_cat})