from django.shortcuts import render, redirect, get_object_or_404
from .models import Celular, Blog, Carrito, CarritoItem
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

# No funcionó
#def catalogo(request):
 #   with connection.cursor() as cursor:
   #     cursor.execute("SELECT * FROM TecnoMovilApp_celular")
    #    celulares = cursor.fetchall()
  #  return render(request, 'vistas/catalogo.html', {'celulares': celulares})
    
def contacto(request):
    return render(request, 'vistas/Form.html')

#Carrito#
def agregar_al_carrito(request, celular_id):
    celular = get_object_or_404(Celular, id=celular_id)
    carrito_id = request.session.get('carrito_id')
    if not carrito_id:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
    else:
        carrito = Carrito.objects.get(id=carrito_id)

    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, celular=celular)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    
    return redirect('carrito')

def carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        items = CarritoItem.objects.filter(carrito=carrito)
    else:
        items = []
    total = sum(item.subtotal() for item in items)
    return render(request, 'carrito.html', {'items': items, 'total': total})

def vaciar_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        CarritoItem.objects.filter(carrito=carrito).delete()
    return redirect('carrito')