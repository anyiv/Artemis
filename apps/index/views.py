from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from apps.usuario.models import User
from apps.usuario.forms import CrearUsuario
from django.views.generic import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from Artemis.mixin import LoginAuthenticatedMixin

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

def changepassword(request):
    return render(request, 'index/changepassword.html', {})