from django.shortcuts import render

# Create your views here.

def checkpetition(request):
    return render(request, 'peticion/checkpetition.html', {})

def createpetition(request):
    return render(request, 'peticion/createpetition.html', {})

def atc_createpetition(request):
    return render(request, 'peticion/atc_createpetition.html', {})