from django.urls import path
from . import views

urlpatterns = [
    path('consultar/', views.consultpetition, name='consultpetition'),
    path('lista/', views.petitionlist, name='petitionlist'),
]