from django.urls import path
from . import views

urlpatterns = [
    path('checker/', views.dashboard_checker, name='dashboard_checker'),
    path('gestorR/', views.dashboard_gestorR, name='dashboard_gestorR'),
    path('cliente/', views.dashboard_cliente, name='dashboard_cliente'),
]