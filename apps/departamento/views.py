from django.shortcuts import render

# Create your views here.
def createdep(request):
    return render(request, 'departamento/createdep.html', {})
