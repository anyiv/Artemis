from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.claimlist, name='claimlist'),
    path('listadadofinalizados/', views.claimfinished, name='claimfinished'),
    path('reclamosproxavencer/', views.claimexpire, name='claimexpire'),
    path('registrar/', views.createclaim, name='createclaim'),
]