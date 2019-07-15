from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.petitionlist, name='petitionlist'),
    path('consultar/',views.checkpetition, name='checkpetition'),
    path('registrar/',views.createpetition, name='createpetition'),
    path('atc_registrar/',views.atc_createpetition, name='atc_createpetition'),
]