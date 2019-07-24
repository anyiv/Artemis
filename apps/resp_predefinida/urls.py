from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.createpredanswer.as_view(), name='createpredanswer'),
    path('lista/',views.predanswerlist.as_view(), name='predanswerlist'),
    path('consulta/<pk>/', views.checkpredanswer.as_view(), name='checkpredanswer'),
    path('modificar/<pk>/', views.updatepredanswer.as_view(), name='updatepredanswer'),
]