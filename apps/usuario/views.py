from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import User, TipoUser
from .forms import ActualizarUsuarioForm, CrearUsuario, ConsultarEmpleado, ConsultarCliente
from apps.datos_externos.models import Empleado, Cliente
from apps.reclamo.models import Categoria, Reclamo
from apps.pqs.models import PQS
from apps.resp_predefinida.models import RespuestaPredefinida
from django.contrib.messages.views import SuccessMessageMixin
from Artemis.mixin import *


# Create your views here.

def dashboard_checker(request):
    if request.user.codTipoUser.codTipoUser == 'cli':
        return redirect('inicio/cliente/')
    elif request.user.codTipoUser.codTipoUser == 'grec':
        return redirect('inicio/gestreclamo/')
    elif request.user.codTipoUser.codTipoUser == 'atc':
        return redirect('inicio/atencioncli/')
    elif request.user.codTipoUser.codTipoUser == 'gpqs':
        return redirect('inicio/gestorPQS/')
    elif request.user.codTipoUser.codTipoUser == 'tc':
        return redirect('inicio/tecnico/')
    elif request.user.codTipoUser.codTipoUser == 'admin':
        return redirect('inicio/admin/')
    elif request.user.codTipoUser.codTipoUser == 'ger':
        return redirect('inicio/gerente/')

class dashboard_gestreclamo(AuthenticatedGestorReclamosMixin, DetailView):
    model = Reclamo
    template_name = "usuario/gestreclamo/dashboard_gestreclamo.html"

class dashboard_cliente(AuthenticatedClienteMixin, ListView):
    model = Reclamo
    template_name = "usuario/cliente/dashboard_cliente.html"

    def get_context_data(self, **kwargs):
        context = super(dashboard_cliente, self).get_context_data(**kwargs)
        context['object_list'] = Reclamo.objects.filter(nombreUsuario = self.request.user.nombreUsuario, estatus = 'P')
        return context

class dashboard_atencioncli(AuthenticatedAtClienteMixin, ListView):
    model = User
    template_name = "usuario/atencioncli/dashboard_atencioncli.html"
    
    def get_context_data(self, **kwargs):
        context = super(dashboard_atencioncli, self).get_context_data(**kwargs)
        context['cant_pet'] = PQS.objects.filter(categoria='P').count()
        context['cant_que'] = PQS.objects.filter(categoria='Q').count()
        context['cant_rec'] = Reclamo.objects.count()
        context['cant_sug'] = PQS.objects.filter(categoria='S').count()
        pqs = PQS.objects.values('codPQS','nombreUsuario','fechaRegistro','categoria','estatus')
        reclamo = Reclamo.objects.values('codReclamo','nombreUsuario','fechaRegistro','codCategoria','estatus')
        context['object_list'] = pqs.union(reclamo).order_by('-fechaRegistro')
        return context


def dashboard_gestorPQS(request):
    return render(request, 'usuario/gestpqs/dashboard_gestorpqs.html', {})

def dashboard_tecnico(request):
    return render(request, 'usuario/tecnico/dashboard_tecnico.html', {})

class dashboard_admin(AuthenticatedAdminMixin, ListView):
    model = User
    template_name = "usuario/admin/dashboard_admin.html"

    def get_context_data(self, **kwargs):
        context = super(dashboard_admin, self).get_context_data(**kwargs)
        context['cant_categorias'] = Categoria.objects.filter(estatus='A').count()
        context['cant_empleados'] = Empleado.objects.filter(estatus='A').count()
        context['cant_clientes'] = Cliente.objects.filter(estatus='A').count()
        context['cant_rp'] = RespuestaPredefinida.objects.filter(estatus='A').count()
        return context

def dashboard_gerente(request):
    return render(request, 'usuario/gerente/dashboard_gerente.html', {})

class createemployee(AuthenticatedAdminMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = CrearUsuario
    template_name = "usuario/empleado/createemployee.html"
    success_url = reverse_lazy('createemployee')
    success_message = "e"

    def get_context_data(self, **kwargs):
        context = super(createemployee, self).get_context_data(**kwargs)
        context['tipousers'] = TipoUser.objects.filter(estatus='A').exclude(codTipoUser='cli')
        return context

def pqslist(request):
    return render(request, 'usuario/gestpqs/pqslist.html', {})

def pqrslist(request):
    return render(request, 'usuario/atencioncli/pqrslist.html', {})

def profile(request):
    return render(request, 'usuario/profile.html', {})

class updateprofile(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ActualizarUsuarioForm
    template_name = "usuario/updateprofile.html"
    success_url = reverse_lazy('profile')
    success_message = "e"

    def get_object(self, queryset=None):
        return self.request.user

class employeelist(AuthenticatedAdminMixin, ListView):
    model = User
    template_name = "usuario/empleado/employeelist.html"

    def get_context_data(self, **kwargs):
        context = super(employeelist, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(idCliente = None, estatus='A')
        return context

class checkemployee(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ConsultarEmpleado
    template_name = "usuario/empleado/checkemployee.html"
    success_url = reverse_lazy('employeelist')
    success_message = "e"
    
    def get_context_data(self, **kwargs):
        context = super(checkemployee, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['empleado'] = User.objects.get(nombreUsuario = pk)
        context['user'] = self.request.user
        return context

class clientlist(AuthenticatedAdminMixin, ListView):
    model = User
    template_name = "usuario/cliente/clientlist.html"

    def get_context_data(self, **kwargs):
        context = super(clientlist, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(idEmpleado = None)
        return context        

class checkclient(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ConsultarCliente
    template_name = "usuario/cliente/checkclient.html"
    success_url = reverse_lazy('clientlist')
    success_message = "e"

    def get_context_data(self, **kwargs):
        context = super(checkclient, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['cliente'] = User.objects.get(nombreUsuario = pk)
        context['user'] = self.request.user
        return context

#CONSULTAR PQRS DEL CLIENTE
class checkpqrslist(AuthenticatedClienteMixin, ListView):
    model = PQS
    template_name = "usuario/cliente/checkpqrslist.html"
    
    def get_context_data(self, **kwargs):
        context = super(checkpqrslist, self).get_context_data(**kwargs)
        pqs = PQS.objects.filter(nombreUsuario=self.request.user.nombreUsuario).values('codPQS','descripcion','fechaRegistro','categoria','estatus')
        reclamo = Reclamo.objects.filter(nombreUsuario=self.request.user.nombreUsuario).values('codReclamo','descripcion','fechaRegistro','codCategoria','estatus')
        context['object_list'] = pqs.union(reclamo).order_by('-fechaRegistro')
        return context