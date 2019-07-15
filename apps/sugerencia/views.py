from django.shortcuts import render

# Create your views here.

def suggestionlist(request):
    return render(request, 'sugerencia/suggestionlist.html', {})

def createsuggestion(request):
    return render(request, 'sugerencia/createsuggestion.html', {})