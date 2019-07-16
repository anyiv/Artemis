from django.shortcuts import render

# Create your views here.

def petitionlist(request):
    return render(request, 'peticion/petitionlist.html', {})

def checkpetition(request):
    return render(request, 'peticion/checkpetition.html', {})

def createpetition(request):
    return render(request, 'peticion/createpetition.html', {})

def atc_createpetition(request):
    return render(request, 'peticion/atc_createpetition.html', {})