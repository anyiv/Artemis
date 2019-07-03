from django.urls import path
from . import views

urlpatterns = [
    path('suggestionlist/', views.suggestionlist, name='suggestionlist'),
]