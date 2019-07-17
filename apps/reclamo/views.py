from django.shortcuts import render

# Create your views here.

def claimlist(request):
    return render(request, 'reclamo/claimlist.html', {})

def claimfinished(request):
    return render(request, 'reclamo/claimfinished.html', {})

def claimexpire(request):
    return render(request, 'reclamo/claimexpire.html', {})

def createclaim(request):
    return render(request, 'reclamo/createclaim.html', {})

def atc_createclaim(request):
    return render(request, 'reclamo/atc_createclaim.html', {})

def checkclaim(request):
    return render(request, 'reclamo/checkclaim.html', {})

def createclaimcategory(request):
    return render(request, 'reclamo/createclaimcategory.html', {})

def attendclaim(request):
    return render(request, 'reclamo/attendclaim.html', {})