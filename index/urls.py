from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('logout/', views.logout.as_view(), name='logout'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('signup/', views.signup, name='signup'),
]
