from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_checker, name='dashboard_checker'),
    path('gestreclamo/', views.dashboard_gestreclamo, name='dashboard_gestreclamo'),
    path('cliente/', views.dashboard_cliente, name='dashboard_cliente'),
    path('atencioncli/', views.dashboard_atencioncli, name='dashboard_atencioncli'),
    path('gestorPQS/', views.dashboard_gestorPQS, name='dashboard_gestorPQS'),
    path('tecnico/', views.dashboard_tecnico, name='dashboard_tecnico'),
    path('admin/', views.dashboard_admin, name='dashboard_admin'),
    path('gerente/', views.dashboard_gerente, name='dashboard_gerente'),
    path('crear/', views.createemploy, name='createemploy'),
]