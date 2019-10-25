from django.urls import path
from . import views

urlpatterns = [
    path('peticion/registrar/',views.cli_crearpeticion.as_view(), name='cli_crearpeticion'),
    path('peticion/atc_registrar/',views.atc_crearpeticion.as_view(), name='atc_crearpeticion'),
    path('queja/registrar/', views.cli_crearqueja.as_view(), name='cli_crearqueja'),
    path('queja/atc_registrar/', views.atc_crearqueja.as_view(), name='atc_crearqueja'),
    path('sugerencia/registrar/', views.cli_crearsugerencia.as_view(), name='cli_crearsugerencia'),
    path('sugerencia/atc_registrar/', views.atc_crearsugerencia.as_view(), name='atc_crearsugerencia'),
    path('consulta/<pk>/', views.consultarpqs.as_view(), name='consultarpqs'),
    path('atender/<pk>/', views.atenderpqs.as_view(), name='atenderpqs'),
    path('reporte/marcadas/',views.reporte_pqsmarcados.as_view(), name='reporte_pqsmarcados'),
    path('marcadas/',views.pqsmarcados.as_view(), name='pqsmarcados'),
    path('pqs/lista/', views.g_listapqs.as_view(), name='g_listapqs'),
]