from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.createpredanswer, name='createpredanswer'),
]