from django.urls import path
from . import views

urlpatterns = [
    path('sincronizar/datos_externos/', views.externaldata, name='externaldata'),
]