from django.shortcuts import render

# Create your views here.
def complaintlist(request):
    return render(request, 'queja/complaintlist.html', {})
