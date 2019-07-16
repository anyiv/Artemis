from django.shortcuts import render

# Create your views here.

def createpredanswer(request):
    return render(request, 'resp_predefinida/createpredanswer.html', {})

def predanswerlist(request):
    return render(request, 'resp_predefinida/predanswerlist.html', {})
