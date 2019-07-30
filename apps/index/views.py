from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from apps.usuario.models import User
from apps.datos_externos.models import Cliente
from apps.usuario.forms import CrearUsuario
from django.views.generic import UpdateView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from Artemis.mixin import LoginAuthenticatedMixin, LoginRequiredMixin
from .forms import CambiarContraseña
from django.http import JsonResponse

#Vista que valida que un cliente esté registrado en el sistema para que un usuario
#atención al cliente pueda crear un PQRS para él.

def validar_cliente(request):
    identidad = request.POST.get('identificacion', None)

    ce = Cliente.objects.filter(identificacion=identidad).exists()
    cliente = usuario = None

    if ce:
        cliente = Cliente.objects.get(identificacion=identidad)
    
    ue = User.objects.filter(idCliente=identidad).exists()
    
    if ue:
        usuario = User.objects.get(idCliente=identidad)
    
    if usuario and cliente:
        data = {
            'cliente_existe' : ce,
            'usuario_existe' : ue,
            'nombre_usuario' : usuario.nombreUsuario,
            'nombre' : cliente.nombre,
            'apellido' : cliente.apellido,
            'direccion' : cliente.direccion
        }
    else:
        data = {
            'cliente_existe' : ce,
            'usuario_existe' : ue
        }
    return JsonResponse(data)

class index(LoginAuthenticatedMixin, LoginView):
    template_name = 'index/index.html'

class logout(LogoutView):
    template_name = 'index/logout.html'

class signup(LoginAuthenticatedMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = CrearUsuario
    template_name = "index/signup.html"
    success_url = reverse_lazy('index')
    success_message = "u"

# class changepassword(LoginRequiredMixin, FormView):
#     model = User
#     form_class = CambiarContraseña
#     template_name = "index/changepassword.html"

#     def get_form_kwargs(self):
#         kwargs = super(changepassword, self).get_form_kwargs()
#         kwargs['user'] = User.objects.filter(pk = self.request.user.nombreUsuario)
#         return kwargs

def changepassword(request):
    return render(request, 'index/changepassword.html', {})