from django.shortcuts import render

# Create your views here.
def externaldata(request):
    return render(request, 'datos_externos/externaldata.html', {})
