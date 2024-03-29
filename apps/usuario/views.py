from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import User, TipoUser
from .forms import ActualizarUsuarioForm, CrearUsuario, ConsultarEmpleado, ConsultarCliente
from apps.datos_externos.models import Empleado, Cliente
from apps.reclamo.models import Categoria, Reclamo
from apps.pqs.models import PQS
from apps.resp_predefinida.models import RespuestaPredefinida
from django.contrib.messages.views import SuccessMessageMixin
from Artemis.mixin import *
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect

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

#INICIOS DE USUARIOS
class inicio_gestreclamo(AuthenticatedGestorReclamosMixin, ListView):
    model = Reclamo
    template_name = "usuario/gestreclamo/inicio_gestreclamo.html"

    def get_context_data(self, **kwargs):
        context = super(inicio_gestreclamo, self).get_context_data(**kwargs)
        fecha_tope = datetime.now() + timedelta(days=7)
        reclamos = Reclamo.objects.filter(responsableReclamo=self.request.user)
        context['object_list'] = reclamos.filter(estatus = 'P')
        context['contrec'] = reclamos.filter(estatus = 'P').count()
        context['recfin'] = reclamos.filter(estatus='F').count()
        context['cantpav'] = reclamos.filter(fechaEstimada__lte=fecha_tope).exclude(estatus='F').count()
        return context

class inicio_cliente(AuthenticatedClienteMixin, ListView):
    model = Reclamo
    template_name = "usuario/cliente/inicio_cliente.html"

    def get_context_data(self, **kwargs):
        context = super(inicio_cliente, self).get_context_data(**kwargs)
        context['object_list'] = Reclamo.objects.filter(nombreUsuario = self.request.user.nombreUsuario, estatus = 'P')
        return context

class inicio_atencioncli(AuthenticatedAtClienteMixin, ListView):
    model = User
    template_name = "usuario/atencioncli/inicio_atencioncli.html"
    
    def get_context_data(self, **kwargs):
        context = super(inicio_atencioncli, self).get_context_data(**kwargs)
        pqs = PQS.objects.values('codPQS','nombreUsuario','fechaRegistro','categoria','estatus')
        reclamo = Reclamo.objects.values('codReclamo','nombreUsuario','fechaRegistro','codCategoria','estatus')
        context['object_list'] = pqs.union(reclamo).order_by('-fechaRegistro')
        return context

class inicio_gestorpqs(ListView):
    model = PQS
    template_name = "usuario/gestpqs/inicio_gestorpqs.html"
    
    def get_context_data(self, **kwargs):
        context = super(inicio_gestorpqs, self).get_context_data(**kwargs)
        pqs = PQS.objects.all()
        context['object_list'] = pqs.all().reverse()
        context['cant_pen'] = pqs.filter(estatus='P').count()
        context['cant_mar'] = pqs.filter(estatus='M').count()
        context['cant_sug'] = pqs.filter(estatus='P').count()
        return context

class inicio_tecnico(ListView):
    model = Reclamo
    template_name = "usuario/tecnico/inicio_tecnico.html"

    def get_context_data(self, **kwargs):
        context = super(inicio_tecnico, self).get_context_data(**kwargs)
        context['object_list'] = Reclamo.objects.filter(responsableReclamo = self.request.user.nombreUsuario, estatus = 'P')
        return context

class inicio_admin(AuthenticatedAdminMixin, ListView):
    model = User
    template_name = "usuario/admin/inicio_admin.html"

    def get_context_data(self, **kwargs):
        context = super(inicio_admin, self).get_context_data(**kwargs)
        user = User.objects.filter(estatus='A')
        context['cant_categorias'] = Categoria.objects.filter(estatus='A').count()
        context['cant_empleados'] = user.filter(idCliente=None).count()
        context['cant_clientes'] = user.filter(idEmpleado=None).count()
        context['cant_rp'] = RespuestaPredefinida.objects.filter(estatus='A').count()
        return context

def inicio_gerente(request):
    return render(request, 'usuario/gerente/inicio_gerente.html', {})

#EMPLEADOS
class crear_empleado(AuthenticatedAdminMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = CrearUsuario
    template_name = "usuario/empleado/crear_empleado.html"
    success_url = reverse_lazy('crear_empleado')
    success_message = "e"

    def get_context_data(self, **kwargs):
        context = super(crear_empleado, self).get_context_data(**kwargs)
        context['tipousers'] = TipoUser.objects.filter(estatus='A').exclude(codTipoUser='cli')
        return context

class lista_empleados(AuthenticatedAdminMixin, ListView):
    model = User
    template_name = "usuario/empleado/lista_empleados.html"

    def get_context_data(self, **kwargs):
        context = super(lista_empleados, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(idCliente = None, estatus='A')
        return context

class consultar_empleado(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ConsultarEmpleado
    template_name = "usuario/empleado/consultar_empleado.html"
    success_url = reverse_lazy('lista_empleados')
    success_message = "e"
    
    def get_context_data(self, **kwargs):
        context = super(consultar_empleado, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['empleado'] = User.objects.get(nombreUsuario = pk)
        context['user'] = self.request.user
        return context

#CLIENTES
class listacliente(AuthenticatedAdminMixin, ListView):
    model = User
    template_name = "usuario/cliente/listacliente.html"

    def get_context_data(self, **kwargs):
        context = super(listacliente, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(idEmpleado = None, estatus="A")
        return context        

class consultarcliente(AuthenticatedAdminMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ConsultarCliente
    template_name = "usuario/cliente/consultarcliente.html"
    success_url = reverse_lazy('listacliente')
    success_message = "e"

    def get_context_data(self, **kwargs):
        context = super(consultarcliente, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['cliente'] = User.objects.get(nombreUsuario = pk)
        context['user'] = self.request.user
        return context


#PERFIL
def perfil(request):
    return render(request, 'usuario/perfil.html', {})

class modificar_perfil(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ActualizarUsuarioForm
    template_name = "usuario/modificar_perfil.html"
    success_url = reverse_lazy('perfil')
    success_message = "e"

    def get_object(self, queryset=None):
        return self.request.user

#CONSULTAR PQRS DEL CLIENTE
class lista_pqrscliente(AuthenticatedClienteMixin, ListView):
    model = PQS
    template_name = "usuario/cliente/lista_pqrscliente.html"
    
    def get_context_data(self, **kwargs):
        context = super(lista_pqrscliente, self).get_context_data(**kwargs)
        pqs = PQS.objects.filter(nombreUsuario=self.request.user.nombreUsuario).values('codPQS','descripcion','fechaRegistro','categoria','estatus')
        reclamo = Reclamo.objects.filter(nombreUsuario=self.request.user.nombreUsuario).values('codReclamo','descripcion','fechaRegistro','codCategoria','estatus')
        context['object_list'] = pqs.union(reclamo).order_by('-fechaRegistro')
        return context

#REPORTES DEL GERENTE
class reporte_fallas(TemplateView):
    template_name = 'usuario/gerente/reporte_fallas.html'

class reporte_encuestas(TemplateView):
    template_name = 'usuario/gerente/reporte_encuestas.html'

class reporte_pqs(ListView):
    model = PQS
    template_name = "usuario/gerente/reporte_pqs.html"

    def get_context_data(self, **kwargs):
        context = super(reporte_pqs, self).get_context_data(**kwargs)
        context['object_list'] = PQS.objects.filter(estatus='M')
        return context

class lista_notificaciones(LoginRequiredMixin, TemplateView):
    template_name = "usuario/notificaciones.html"

    def get_context_data(self, **kwargs):
        context = super(lista_notificaciones, self).get_context_data(**kwargs)
        context['notificaciones'] = self.request.user.notifications.all()
        return context