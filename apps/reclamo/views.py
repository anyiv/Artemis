from django.shortcuts import render

# Create your views here.

def claimlist(request):
    return render(request, 'reclamo/claimlist.html', {})