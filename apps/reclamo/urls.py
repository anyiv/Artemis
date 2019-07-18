from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.claimlist, name='claimlist'),
    path('lista/finalizados/', views.claimfinished, name='claimfinished'),
    path('lista/proximovencimiento', views.claimexpire, name='claimexpire'),
    path('registrar/', views.createclaim, name='createclaim'),
    path('atc_registrar/', views.atc_createclaim, name='atc_createclaim'),
    path('categoría/crear', views.createclaimcategory, name='createclaimcategory'),
    path('consultar/', views.checkclaim, name='checkclaim'),
    path('atender/', views.attendclaim, name='attendclaim'),
    path('categorias/lista', views.claimcategorylist, name='claimcategorylist'),
    path('categoria/lista', views.checkclaimcategory, name='checkclaimcategory'),
    path('satisfaccion/lista', views.finishedclaimlist, name='finishedclaimlist'),
    path('satisfaccion/encuesta', views.satisfactionsurvey, name='satisfactionsurvey'),
]