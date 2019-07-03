from django.shortcuts import render

# Create your views here.

def petitionlist(request):
    return render(request, 'peticion/petitionlist.html', {})