from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.complaintlist, name='complaintlist'),
    path('registrar/', views.createcomplaint, name='createcomplaint'),
]