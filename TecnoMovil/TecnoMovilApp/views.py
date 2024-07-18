from django.shortcuts import render
from .models import Celular, Blog
from django.db import connection
from random import sample

def index(request):
    todos_los_celulares = list(Celular.objects.all())
    celulares_mostrados = sample(todos_los_celulares, 3) if len(todos_los_celulares) >= 3 else todos_los_celulares
    
    blogs = Blog.objects.all()
    
    context = {
        'celulares_mostrados': celulares_mostrados,
        'blogs': blogs
    }
    
    return render(request, 'index.html', context)

def catalogo(request):
    celulares = Celular.objects.all() 
    return render(request, 'vistas/catalogo.html', {'celulares': celulares})

#def catalogo(request):
 #   with connection.cursor() as cursor:
   #     cursor.execute("SELECT * FROM TecnoMovilApp_celular")
    #    celulares = cursor.fetchall()
  #  return render(request, 'vistas/catalogo.html', {'celulares': celulares})
    
def contacto(request):
    return render(request, 'vistas/Form.html')