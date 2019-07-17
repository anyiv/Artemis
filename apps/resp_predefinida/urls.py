from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.createpredanswer, name='createpredanswer'),
    path('listado/',views.predanswerlist, name='predanswerlist'),
]