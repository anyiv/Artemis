from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'usuario/dashboard.html', {})

def petitionlist(request):
    return render(request, 'peticion/petitionlist.html', {})

def complaintlist(request):
    return render(request, 'queja/complaintlist.html', {})

def claimlist(request):
    return render(request, 'reclamo/claimlist.html', {})

def suggestionlist(request):
    return render(request, 'sugerencia/suggestionlist.html', {})