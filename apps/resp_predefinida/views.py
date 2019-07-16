from django.shortcuts import render

# Create your views here.

def createpredanswer(request):
    return render(request, 'resp_predefinida/createpredanswer.html', {})
