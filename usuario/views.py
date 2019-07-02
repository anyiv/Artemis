from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'usuario/dashboard.html', {})

def petitionlist(request):
    return render(request, 'peticion/petitionlist.html', {})