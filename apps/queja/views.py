from django.shortcuts import render

# Create your views here.
def createcomplaint(request):
    return render(request, 'queja/createcomplaint.html', {})

def atc_createcomplaint(request):
    return render(request, 'queja/atc_createcomplaint.html', {})
