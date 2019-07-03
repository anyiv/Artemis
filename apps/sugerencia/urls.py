from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.suggestionlist, name='suggestionlist'),   
]