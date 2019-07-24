from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('lista/', views.claimlist, name='claimlist'),
    path('lista/finalizados/', views.claimfinished, name='claimfinished'),
    path('lista/proximovencimiento', views.claimexpire, name='claimexpire'),
    path('registrar/', views.createclaim, name='createclaim'),
    path('atc_registrar/', views.atc_createclaim, name='atc_createclaim'),
    path('consultar/', views.checkclaim, name='checkclaim'),
    path('atender/', views.attendclaim, name='attendclaim'),
    path('categoria/crear', views.createclaimcategory.as_view(), name='createclaimcategory'),
    path('categoria/lista', views.claimcategorylist.as_view(), name='claimcategorylist'),
    path('categoria/consulta/<pk>/', views.checkclaimcategory.as_view(), name='checkclaimcategory'),
    path('categoria/modificar/<pk>/', views.updateclaimcategory.as_view(), name='updateclaimcategory'),
    path('satisfaccion/lista', views.finishedclaimlist, name='finishedclaimlist'),
    path('satisfaccion/encuesta', views.satisfactionsurvey, name='satisfactionsurvey'),
]