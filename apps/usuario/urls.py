from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.dashboard_admin, name='dashboard_adm'),
    path('cliente/', views.dashboard_cliente, name='dashboard_cli'),
]