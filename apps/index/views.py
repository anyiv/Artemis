from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class index(LoginView):
    template_name = 'index/index.html'

class logout(LogoutView):
    template_name = 'index/logout.html'

def forgotpassword(request):
    return render(request, 'index/forgotpassword.html', {})

def signup(request):
    return render(request, 'index/signup.html', {})

def changepassword(request):
    return render(request, 'index/changepassword.html', {})