from django.shortcuts import render

# Create your views here.
def createfailure(request):
    return render(request, 'averia_masiva/createfailure.html', {})