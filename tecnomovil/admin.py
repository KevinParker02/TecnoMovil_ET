from django.contrib import admin
from .models import Celular, Carrito, Categoria

class CelularAdmin(admin.ModelAdmin):
    exclude = ('stock',)

admin.site.register(Celular, CelularAdmin)
admin.site.register(Carrito)
admin.site.register(Categoria)