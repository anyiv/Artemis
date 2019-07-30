from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from apps.usuario.models import User
from apps.usuario.forms import CrearUsuario
from django.views.generic import UpdateView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from Artemis.mixin import LoginAuthenticatedMixin, LoginRequiredMixin
from .forms import CambiarContraseña

# Create your views here.

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