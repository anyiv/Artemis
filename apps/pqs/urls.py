from django.urls import path
from . import views

urlpatterns = [
    path('peticion/registrar/',views.createpetition.as_view(), name='createpetition'),
    path('peticion/atc_registrar/',views.atc_createpetition.as_view(), name='atc_createpetition'),
    path('peticion/consultar/',views.checkpetition, name='checkpetition'),
    path('queja/registrar/', views.createcomplaint.as_view(), name='createcomplaint'),
    path('queja/atc_registrar/', views.atc_createcomplaint, name='atc_createcomplaint'),
    path('sugerencia/registrar/', views.createsuggestion.as_view(), name='createsuggestion'),
    path('sugerencia/atc_registrar/', views.atc_createsuggestion, name='atc_createsuggestion'),
    path('pqs/consulta/<pk>/', views.check_pqs.as_view(), name='check_pqs'),
    path('pqs/atender/<pk>/', views.attendpqs.as_view(), name='attendpqs'),
]