from django.contrib import admin
from .models import Categoria, Celular, Blog

# Register your models here.
admin.site.register(Categoria)
#admin.site.register(Celular)
admin.site.register(Blog)

@admin.register(Celular)
class CelularAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'description', 'precio', 'stock', 'imagen')
    search_fields = ('nombre', 'description')
    list_filter = ('marca', 'precio')

