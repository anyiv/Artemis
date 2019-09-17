from django.shortcuts import render

# Create your views here.
def datos_externos(request):
    return render(request, 'datos_externos/datos_externos.html', {})
