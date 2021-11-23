from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('sesiones/', views.sesiones),
    path('apoyo/', views.apoyo),
]