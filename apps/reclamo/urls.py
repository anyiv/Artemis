from django.urls import path
from . import views

urlpatterns = [
    path('claimlist/', views.claimlist, name='claimlist'),
]