from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('catalogo/', views.catalogo_view, name='catalogo'),
    path('carrito/', views.carrito_view, name='carrito'),
    path('agregar/<int:celular_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
