from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.http import HttpResponseRedirect
from apps.usuario.models import User
from apps.datos_externos.models import Cliente, Contrato, DetalleContrato
from apps.usuario.forms import CrearUsuario
from django.views.generic import UpdateView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from Artemis.mixin import LoginAuthenticatedMixin, LoginRequiredMixin
from .forms import Cambiarcontrasena
from django.http import JsonResponse

#Vista que valida que un cliente esté registrado en el sistema para que un usuario
#atención al cliente pueda crear un PQRS para él.

def validar_cliente(request):
    identidad = request.POST.get('identificacion', None)

    ce = Cliente.objects.filter(identificacion=identidad,estatus='A').exists()
    cliente = usuario = None

    if ce:
        cliente = Cliente.objects.get(identificacion=identidad)
    
    ue = User.objects.filter(idCliente=identidad).exists()
    
    if ue:
        usuario = User.objects.get(idCliente=identidad)
    
    if usuario and cliente:
        detalle_contrato = []

        try:
            contrato = Contrato.objects.get(codCliente = cliente)
            detcon = DetalleContrato.objects.filter(nroContrato = contrato)
            for d in detcon:
                detalle_contrato.append((
                    d.codDetContrato,
                    d.codServicio.nombre
                ))
        except:
            pass

        data = {
            'cliente_existe' : ce,
            'usuario_existe' : ue,
            'nombre_usuario' : usuario.nombreUsuario,
            'nombre' : cliente.nombre,
            'apellido' : cliente.apellido,
            'direccion' : cliente.direccion,
            'servicios' : detalle_contrato
        }
    else:
        data = {
            'cliente_existe' : ce,
            'usuario_existe' : ue
        }
    return JsonResponse(data)

class index(LoginAuthenticatedMixin, SuccessMessageMixin, LoginView):
    template_name = 'index/index.html'

    def form_valid(self, form):
        if form.get_user().codTipoUser.codTipoUser == "grec":
            form.get_user().login_grec()
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

class logout(LogoutView):
    template_name = 'index/logout.html'

class signup(LoginAuthenticatedMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = CrearUsuario
    template_name = "index/signup.html"
    success_url = reverse_lazy('signup')
    success_message = "u"

# class cambiar_contrasena(LoginRequiredMixin, FormView):
#     model = User
#     form_class = Cambiarcontrasena
#     template_name = "index/cambiar_contrasena.html"

#     def get_form_kwargs(self):
#         kwargs = super(cambiar_contrasena, self).get_form_kwargs()
#         kwargs['user'] = User.objects.filter(pk = self.request.user.nombreUsuario)
#         return kwargs

def cambiar_contrasena(request):
    return render(request, 'index/cambiar_contrasena.html', {})