from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.createcomplaint, name='createcomplaint'),
    path('atc_registrar/', views.atc_createcomplaint, name='atc_createcomplaint'),
]