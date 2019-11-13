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
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
import notifications.urls

urlpatterns = [
    path('', include('apps.index.urls')),
    path('', include('pwa.urls')),
    path('djangoadmin/', admin.site.urls),
    path('usuario/', include('apps.usuario.urls')),
    path('reclamo/', include('apps.reclamo.urls')),
    path('resp_predefinida/', include('apps.resp_predefinida.urls')),
    path('pqs/', include('apps.pqs.urls')),
    path('datosexternos/', include('apps.datos_externos.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)