from django.urls import path
from . import views
from django.contrib.auth.views import  PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('registrarse/', views.signup.as_view(), name='signup'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('cambiarcontrasenna/', views.cambiar_contrasena, name='cambiar_contrasena'),
    path('recuperar_credenciales/', PasswordResetView.as_view(html_email_template_name='registration/password_reset_email.html'), name='reset'),
    path('cambiarclave/<uidb64>/<token>/', PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    path('correo_enviado/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('contrasenna_cambiada/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('ajax/validar_identidad/', views.validar_cliente, name='validar_cliente'),
    path('ajax/asignar_tecnico/', views.asignar_tecnico, name='asignar_tecnico'),
    path('ajax/obtener_respuesta/', views.obtener_respuesta, name='obtener_respuesta'),
    path('ajax/enviar_rp/', views.enviar_rp, name='enviar_respuesta'),
    path('ajax/obtener_rp_pqs/', views.obt_rp_pqs, name='obtener_rp_pqs'),
    path('ajax/enviar_rp_pqs/', views.enviar_rp_pqs, name='enviar_rp_pqs'),
]
