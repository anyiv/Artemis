from django.urls import path
from . import views

urlpatterns = [
     path('crear/', views.createfailure, name='createfailure'),
     path('listado/', views.failurelist, name='failurelist'),

]