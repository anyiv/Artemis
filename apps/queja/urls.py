from django.urls import path
from . import views

urlpatterns = [
    path('complaintlist/', views.complaintlist, name='complaintlist'),
]