from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy
from .models import User, TipoUser
from .forms import ActualizarUsuarioForm, CrearUsuario, ConsultarEmpleado
from apps.datos_externos.models import Empleado, Cliente
from apps.reclamo.models import Categoria
from apps.resp_predefinida.models import RespuestaPredefinida
from django.contrib.messages.views import SuccessMessageMixin


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

def dashboard_gestreclamo(request):
    return render(request, 'usuario/gestreclamo/dashboard_gestreclamo.html', {})

def dashboard_cliente(request):
    return render(request, 'usuario/cliente/dashboard_cliente.html', {})

def dashboard_atencioncli(request):
    return render(request, 'usuario/atencioncli/dashboard_atencioncli.html', {})

def dashboard_gestorPQS(request):
    return render(request, 'usuario/gestpqs/dashboard_gestorpqs.html', {})

def dashboard_tecnico(request):
    return render(request, 'usuario/tecnico/dashboard_tecnico.html', {})

class dashboard_admin(ListView):
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

class createemployee(SuccessMessageMixin, CreateView):
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

class updateprofile(SuccessMessageMixin, UpdateView):
    model = User
    form_class = ActualizarUsuarioForm
    template_name = "usuario/updateprofile.html"
    success_url = reverse_lazy('profile')
    success_message = "e"

    def get_object(self, queryset=None):
        return self.request.user

class clientlist(ListView):
    model = User
    template_name = "usuario/cliente/clientlist.html"

    def get_context_data(self, **kwargs):
        context = super(clientlist, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(idEmpleado = None)
        return context

def clientlist_pqs(request):
    return render(request, 'usuario/cliente/clientlist_pqs.html',{})

def checkclient(request):
    return render(request, 'usuario/cliente/checkclient.html',{})

class employeelist(ListView):
    model = User
    template_name = "usuario/empleado/employeelist.html"

    def get_context_data(self, **kwargs):
        context = super(employeelist, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.filter(idCliente = None, estatus='A')
        return context

class checkemployee(SuccessMessageMixin, UpdateView):
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