from django.urls import path
from . import views
from django.contrib.auth.views import  PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('registrarse/', views.signup.as_view(), name='signup'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('cambiarcontrasenna/', views.changepassword, name='changepassword'),
    path('recuperar_credenciales/', PasswordResetView.as_view(), name='reset'),
    path('cambiarclave/<uidb64>/<token>/', PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    path('correo_enviado/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('contrasenna_cambiada/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
