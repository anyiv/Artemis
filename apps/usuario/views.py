from django.shortcuts import render

# Create your views here.

def dashboard_checker(request):
    #aqui va un codigo que aun no pienso
    return render(request, 'usuario/gestreclamo/dashboard_gestorR.html', {})    

def dashboard_gestorR(request):
    return render(request, 'usuario/gestreclamo/dashboard_gestorR.html', {})

def dashboard_cliente(request):
    return render(request, 'usuario/cliente/dashboard_cliente.html', {})



