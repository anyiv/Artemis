from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_checker, name='dashboard_checker'),
    path('inicio/gestreclamo/', views.dashboard_gestreclamo, name='dashboard_gestreclamo'),
    path('inicio/cliente/', views.dashboard_cliente.as_view(), name='dashboard_cliente'),
    path('inicio/atencioncli/', views.dashboard_atencioncli, name='dashboard_atencioncli'),
    path('inicio/gestorPQS/', views.dashboard_gestorPQS, name='dashboard_gestorPQS'),
    path('inicio/tecnico/', views.dashboard_tecnico, name='dashboard_tecnico'),
    path('inicio/admin/', views.dashboard_admin.as_view(), name='dashboard_admin'),
    path('inicio/gerente/', views.dashboard_gerente, name='dashboard_gerente'),
    path('empleados/crear/', views.createemployee.as_view(), name='createemployee'),
    path('pqs/lista/', views.pqslist, name='pqslist'),
    path('pqrs/lista/', views.pqrslist, name='pqrslist'),
    path('perfil/', views.profile, name='profile'),
    path('perfil/modificar/', views.updateprofile.as_view(), name='updateprofile'),
    path('clientes/lista/', views.clientlist.as_view(), name='clientlist'),
    path('clientes/ver/<pk>/', views.checkclient.as_view(), name='checkclient'),
    path('empleados/lista/', views.employeelist.as_view(), name='employeelist'),
    path('empleados/ver/<pk>/', views.checkemployee.as_view(), name='checkemployee'),
    path('cliente/pqrs/lista/', views.checkpqrslist.as_view(), name='checkpqrslist'),
]