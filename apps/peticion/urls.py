from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.petitionlist, name='petitionlist'),
    path('consultar/',views.checkpetition, name='checkpetition'),
]