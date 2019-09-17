from django.urls import path
from . import views

urlpatterns = [
    path('sincronizar/datos_externos/', views.datos_externos, name='datos_externos'),
]