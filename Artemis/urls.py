"""Artemis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.index.urls')),
    path('', include('pwa.urls')),
    path('djangoadmin/', admin.site.urls),
    path('usuario/', include('apps.usuario.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('peticion/', include('apps.peticion.urls')),
    path('queja/', include('apps.queja.urls')),
    path('reclamo/', include('apps.reclamo.urls')),
    path('sugerencia/', include('apps.sugerencia.urls')), 
    path('averia_masiva/', include('apps.averia_masiva.urls')),
]
