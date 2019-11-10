from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import IncluirCategoriaForm, ConsultarCategoriaForm, ActualizarCategoriaForm, IncluirReclamo, ConsultarReclamo, AtenderReclamo
from .models import Categoria, Reclamo, HistoricoReclamo
from apps.usuario.models import User
from apps.resp_predefinida.models import RespuestaPredefinida
from apps.datos_externos.models import Contrato, DetalleContrato, Cliente, Servicio
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from Artemis.mixin import AuthenticatedAdminMixin, AuthenticatedClienteMixin, AuthenticatedGPQSAtClienteClienteMixin
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta

# Create your views here.

#RECLAMO
class g_listareclamos(ListView):
    model = Reclamo
    template_name = "reclamo/g_listareclamos.html"

    def get_context_data(self, **kwargs):
        context = super(g_listareclamos, self).get_context_data(**kwargs)
        context['object_list'] = Reclamo.objects.filter(responsableReclamo=self.request.user)
        return context  

class g_reclamosfinalizados(ListView):
    model = Reclamo
    template_name = "reclamo/g_reclamosfinalizados.html"

    def get_context_data(self, **kwargs):
        context = super(g_reclamosfinalizados, self).get_context_data(**kwargs)
        context['object_list'] = Reclamo.objects.filter(responsableReclamo=self.request.user, estatus='F')
        return context
    
class reclamosporvencer(ListView):
    model = Reclamo
    template_name = "reclamo/reclamosporvencer.html"

    def get_context_data(self, **kwargs):
        context = super(reclamosporvencer, self).get_context_data(**kwargs)
        fecha_tope = datetime.now() + timedelta(days=7)
        context['object_list'] = Reclamo.objects.filter(responsableReclamo=self.request.user, fechaEstimada__lte=fecha_tope).exclude(estatus='F')
        return context

class cli_crearReclamo(SuccessMessageMixin, CreateView):
    model = Reclamo
    form_class = IncluirReclamo
    template_name = "reclamo/cli_crearReclamo.html"
    success_url = reverse_lazy('cli_crearReclamo')
    success_message = "e"

    def form_valid(self, form):
        self.object = form.save()
        hr = HistoricoReclamo()
        hr.reclamo = self.object
        hr.detalle = "El reclamo ha sido creado."
        hr.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nuevo reclamo registrado con éxito',
            'Gracias por comunicarnos tu reclamo.',
            'Para nosotros es importante hacerle saber que te valoramos como cliente de nuestra empresa y que estamos trabajando al máximo para que tus problemas sean solucionados cuanto antes.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())

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

    def form_valid(self, form):
        self.object = form.save()
        hr = HistoricoReclamo()
        hr.reclamo = self.object
        hr.detalle = "El reclamo ha sido creado."
        hr.save()
        messages.add_message(self.request,messages.INFO,'e')
        usuario = self.object.nombreUsuario
        usuario.enviarCorreo('Nuevo reclamo registrado con éxito',
            'Gracias por comunicarnos tu reclamo.',
            'Para nosotros es importante hacerle saber que te valoramos como cliente de nuestra empresa y que estamos trabajando al máximo para que tus problemas sean solucionados cuanto antes.',
            'Tu mensaje: ' + self.object.descripcion
        )
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(atc_crearReclamo, self).get_context_data(**kwargs)
        context['catreclamo'] = Categoria.objects.filter(estatus='A')
        return context

class gt_consultarReclamo(UpdateView):
    model = Reclamo
    form_class = ConsultarReclamo
    template_name = "reclamo/gt_consultarReclamo.html"

    def get_context_data(self, **kwargs):
        context = super(gt_consultarReclamo, self).get_context_data(**kwargs)
        context['hist'] = HistoricoReclamo.objects.filter(reclamo=self.kwargs['pk'])
        context['user_cliente'] = User.objects.get(idCliente=context['reclamo'].codDetContrato.nroContrato.codCliente.identificacion)
        tec_asignado = context['reclamo'].responsableReclamo.all().filter(codTipoUser='tc')
        if tec_asignado:
            context['tec_asignado'] = tec_asignado[0].idEmpleado.nombre + ' ' + tec_asignado[0].idEmpleado.apellido
        else:
            context['tec_asignado'] = 'El reclamo no tiene asignado un técnico aún.'
        return context
    

class atenderReclamo(SuccessMessageMixin, UpdateView):
    model = Reclamo
    template_name= "reclamo/atenderReclamo.html"
    form_class = AtenderReclamo

    def form_valid(self, form):
        reclamo_nvo = form.save(commit=False)
        reclamo_viejo = Reclamo.objects.get(codReclamo=self.kwargs['pk'])
        if reclamo_nvo.estatus == "R" and reclamo_viejo.estatus != "R":
            hr = HistoricoReclamo()
            hr.detalle = "El reclamo ha cambiado de estatus de Pendiente a En proceso."
            hr.reclamo = reclamo_viejo
            hr.usuarioEncargado = self.request.user
            hr.save()
        if reclamo_viejo.codCategoria != reclamo_nvo.codCategoria:
            hr = HistoricoReclamo()
            hr.detalle = "El reclamo fue cambiado de categoría a '" + reclamo_nvo.codCategoria.nombre + "'."
            hr.reclamo = reclamo_viejo
            hr.usuarioEncargado = self.request.user
            hr.save()
        if reclamo_nvo.fechaEstimada != reclamo_viejo.fechaEstimada:
            hr = HistoricoReclamo()
            hr.detalle = "La fecha de compromiso fue cambiada."
            hr.reclamo = reclamo_viejo
            hr.usuarioEncargado = self.request.user
            hr.save()
        if reclamo_nvo.estatus == "F":
            reclamo_nvo.fechaFinalizada = datetime.now()
            hr.usuarioEncargado = self.request.user
        reclamo_nvo.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(atenderReclamo, self).get_context_data(**kwargs)
        context['rp'] = RespuestaPredefinida.objects.filter(categoria='rec',estatus='A').order_by('-contUso')
        context['tecnicos'] = User.objects.filter(estatus='A', codTipoUser='tc')
        tec_asignado = context['reclamo'].responsableReclamo.all().filter(codTipoUser='tc')
        if tec_asignado:
            context['tec_asignado'] = tec_asignado[0].idEmpleado.nombre + ' ' + tec_asignado[0].idEmpleado.apellido
        else:
            context['tec_asignado'] = 'El reclamo no tiene asignado un técnico aún.'
        return context

    def get_success_url(self):
        idreclamo=self.kwargs['pk']
        messages.add_message(self.request, messages.INFO, 'e')
        return reverse_lazy('gt_consultarReclamo', kwargs={'pk': idreclamo})

class cli_reclamosfinalizados(ListView):
    model = Reclamo
    template_name = "reclamo/cli_reclamosfinalizados.html"

    def get_context_data(self, **kwargs):
        context = super(cli_reclamosfinalizados, self).get_context_data(**kwargs)
        context['recfin'] =  Reclamo.objects.filter(nombreUsuario=self.request.user, estatus='F')
        return context

def encuesta_cliente(request):
    return render(request, 'reclamo/encuesta_cliente.html', {})

class cli_consultarReclamo(AuthenticatedGPQSAtClienteClienteMixin, DetailView):
    model = Reclamo
    template_name = "reclamo/cli_consultarReclamo.html"

    def get_context_data(self, **kwargs):
        context = super(cli_consultarReclamo, self).get_context_data(**kwargs)
        context['hist'] = HistoricoReclamo.objects.filter(reclamo=self.kwargs['pk'])
        return context

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
