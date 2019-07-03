from django.urls import path
from . import views

urlpatterns = [
    path('lissta/', views.petitionlist, name='petitionlist'),
]