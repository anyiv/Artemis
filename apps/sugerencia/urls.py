from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.createsuggestion, name='createsuggestion'),
    path('atc_registrar/', views.atc_createsuggestion, name='atc_createsuggestion'),
]