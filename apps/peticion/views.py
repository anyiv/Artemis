from django.shortcuts import render

# Create your views here.

def consultpetition(request):
    return render(request, 'peticion/consultpetition.html', {})

def petitionlist(request):
    return render(request, 'peticion/petitionlist.html', {})