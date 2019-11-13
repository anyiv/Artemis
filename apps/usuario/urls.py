from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_checker, name='dashboard_checker'),
    path('inicio/gestreclamo/', views.inicio_gestreclamo.as_view(), name='inicio_gestreclamo'),
    path('inicio/cliente/', views.inicio_cliente.as_view(), name='inicio_cliente'),
    path('inicio/atencioncli/', views.inicio_atencioncli.as_view(), name='inicio_atencioncli'),
    path('inicio/gestorPQS/', views.inicio_gestorpqs.as_view(), name='inicio_gestorpqs'),
    path('inicio/tecnico/', views.inicio_tecnico.as_view(), name='inicio_tecnico'),
    path('inicio/admin/', views.inicio_admin.as_view(), name='inicio_admin'),
    path('inicio/gerente/', views.inicio_gerente, name='inicio_gerente'),
    path('empleados/crear/', views.crear_empleado.as_view(), name='crear_empleado'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/modificar/', views.modificar_perfil.as_view(), name='modificar_perfil'),
    path('clientes/lista/', views.listacliente.as_view(), name='listacliente'),
    path('clientes/ver/<pk>/', views.consultarcliente.as_view(), name='consultarcliente'),
    path('empleados/lista/', views.lista_empleados.as_view(), name='lista_empleados'),
    path('empleados/ver/<pk>/', views.consultar_empleado.as_view(), name='consultar_empleado'),
    path('cliente/pqrs/lista/', views.lista_pqrscliente.as_view(), name='lista_pqrscliente'),
    path('reporte/fallas/', views.reporte_fallas, name='reporte_fallas'),
    path('reporte/satisfaccionclientes/', views.reporte_encuestas, name='reporte_encuestas'),
    path('reporte/pqsmarcadas/', views.reporte_pqs, name='reporte_pqs'),
    path('notificaciones/todas', views.lista_notificaciones.as_view(), name='lista_notificaciones'),
]