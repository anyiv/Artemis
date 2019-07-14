from django.urls import path
from . import views

urlpatterns = [
    path('listadereclamos/', views.claimlist, name='claimlist'),
    path('listadereclamosfinalizados/', views.claimfinished, name='claimfinished'),
     path('reclamosproxavencer/', views.claimexpire, name='claimexpire'),
]