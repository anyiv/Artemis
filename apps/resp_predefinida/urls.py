from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.crear_resp.as_view(), name='crear_resp'),
    path('lista/',views.lista_resp.as_view(), name='lista_resp'),
    path('consulta/<pk>/', views.consultar_resp.as_view(), name='consultar_resp'),
    path('modificar/<pk>/', views.modificar_resp.as_view(), name='modificar_resp'),
]