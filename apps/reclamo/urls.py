from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.claimlist, name='claimlist'),
    path('listadadofinalizados/', views.claimfinished, name='claimfinished'),
    path('reclamosproxavencer/', views.claimexpire, name='claimexpire'),
    path('registrarreclamo/', views.createclaim, name='createclaim'),
]