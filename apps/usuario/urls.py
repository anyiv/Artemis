from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('petitionlist/', views.petitionlist, name='petitionlist'),
    path('complaintlist/', views.complaintlist, name='complaintlist'),
]