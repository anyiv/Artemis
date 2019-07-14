from django.shortcuts import render

# Create your views here.

def claimlist(request):
    return render(request, 'reclamo/claimlist.html', {})

def claimfinished(request):
    return render(request, 'reclamo/claimfinished.html', {})

def claimexpire(request):
    return render(request, 'reclamo/claimexpire.html', {})