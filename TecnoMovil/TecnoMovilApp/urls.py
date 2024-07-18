from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('vistas/catalogo.html', views.catalogo, name='catalogo'),
]
