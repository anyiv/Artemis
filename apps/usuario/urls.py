from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_checker, name='dashboard_checker'),
    path('inicio/gestreclamo/', views.dashboard_gestreclamo, name='dashboard_gestreclamo'),
    path('inicio/cliente/', views.dashboard_cliente, name='dashboard_cliente'),
    path('inicio/atencioncli/', views.dashboard_atencioncli, name='dashboard_atencioncli'),
    path('inicio/gestorPQS/', views.dashboard_gestorPQS, name='dashboard_gestorPQS'),
    path('inicio/tecnico/', views.dashboard_tecnico, name='dashboard_tecnico'),
    path('inicio/admin/', views.dashboard_admin.as_view(), name='dashboard_admin'),
    path('inicio/gerente/', views.dashboard_gerente, name='dashboard_gerente'),
    path('empleados/crear/', views.createemploy, name='createemploy'),
    path('pqs/lista/', views.pqslist, name='pqslist'),
    path('pqrs/lista/', views.pqrslist, name='pqrslist'),
    path('perfil/', views.profile, name='profile'),
    path('perfil/modificar/', views.updateprofile, name='updateprofile'),
    path('clientes/lista/', views.clientlist, name='clientlist'),
    path('pqs/clientes/lista/', views.clientlist_pqs, name='clientlist_pqs'),
    path('clientes/ver/', views.checkclient, name='checkclient'),
    path('empleados/lista/', views.employeelist, name='employeelist'),
    path('empleados/ver/', views.checkemployee, name='checkemployee'),
]