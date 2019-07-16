from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def dashboard_checker(request):
    if request.user.type_u.codigo == 'cli':
        return redirect('cliente/')
    elif request.user.type_u.codigo == 'grec':
        return redirect('gestreclamo/')
    elif request.user.type_u.codigo == 'atc':
        return redirect('atencioncli/')
    elif request.user.type_u.codigo == 'gpqs':
        return redirect('gestorPQS/')
    elif request.user.type_u.codigo == 'tc':
        return redirect('tecnico/')
    elif request.user.type_u.codigo == 'admin':
        return redirect('admin/')
    elif request.user.type_u.codigo == 'ger':
        return redirect('gerente/')

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

def dashboard_admin(request):
    return render(request, 'usuario/admin/dashboard_admin.html', {})

def dashboard_gerente(request):
    return render(request, 'usuario/gerente/dashboard_gerente.html', {})

def createemploy(request):
    return render(request, 'usuario/admin/createemploy.html', {})