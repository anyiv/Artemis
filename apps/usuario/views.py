from django.shortcuts import render

# Create your views here.

def dashboard_checker(request):
    #aqui va un codigo que aun no pienso
    return render(request, 'usuario/dashboard_admin.html', {})    

def dashboard_admin(request):
    return render(request, 'usuario/dashboard_admin.html', {})

def dashboard_cliente(request):
    return render(request, 'usuario/dashboard_cliente.html', {})



