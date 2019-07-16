from django.urls import path
from . import views

urlpatterns = [
    path('listado/', views.claimlist, name='claimlist'),
    path('listadadofinalizados/', views.claimfinished, name='claimfinished'),
    path('reclamosproxavencer/', views.claimexpire, name='claimexpire'),
    path('registrar/', views.createclaim, name='createclaim'),
    path('atc_registrar/', views.atc_createclaim, name='atc_createclaim'),
    path('crearcategoría/', views.createclaimcategory, name='createclaimcategory'),
]