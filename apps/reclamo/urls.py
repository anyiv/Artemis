from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('lista/todos/', views.g_listareclamos.as_view(), name='g_listareclamos'),
    path('lista/finalizados/', views.g_reclamosfinalizados.as_view(), name='g_reclamosfinalizados'),
    path('lista/proximovencimiento/', views.reclamosporvencer, name='reclamosporvencer'),
    path('registrar/', views.cli_crearReclamo.as_view(), name='cli_crearReclamo'),
    path('atc_registrar/', views.atc_crearReclamo.as_view(), name='atc_crearReclamo'),
    path('consultar/<pk>/', views.gt_consultarReclamo.as_view(), name='gt_consultarReclamo'),
    path('atender/<pk>/', views.atenderReclamo.as_view(), name='atenderReclamo'),
    path('categoria/crear/', views.crearcatreclamo.as_view(), name='crearcatreclamo'),
    path('categoria/lista/', views.listacatreclamo.as_view(), name='listacatreclamo'),
    path('categoria/consulta/<pk>/', views.consultarcatreclamo.as_view(), name='consultarcatreclamo'),
    path('categoria/modificar/<pk>/', views.modificarcatreclamo.as_view(), name='modificarcatreclamo'),
    path('satisfaccion/lista/', views.cli_reclamosfinalizados, name='cli_reclamosfinalizados'),
    path('satisfaccion/encuesta/', views.encuesta_cliente, name='encuesta_cliente'),
    path('cliente/consultar/<pk>/', views.cli_consultarReclamo.as_view(), name='cli_consultarReclamo'),
]