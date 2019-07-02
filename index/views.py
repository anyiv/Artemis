from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class index(LoginView):
    template_name = 'index/index.html'

class logout(LogoutView):
    template_name = 'logout.html'