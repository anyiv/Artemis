from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.suggestionlist, name='suggestionlist'),
    path('registrar/', views.createsuggestion, name='createsuggestion'),
]