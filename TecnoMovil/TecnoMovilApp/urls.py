from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('vistas/catalogo.html', views.catalogo, name='catalogo'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:celular_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
]
