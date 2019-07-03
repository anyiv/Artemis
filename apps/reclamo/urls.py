from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.claimlist, name='claimlist'),
]