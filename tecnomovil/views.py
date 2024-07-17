from django.shortcuts import render, get_object_or_404, redirect
from .models import Celular, Carrito
from .forms import AñadirAlCarritoForm

def home(request):
    celulares = Celular.objects.all()  # Obtener todos los celulares
    return render(request, 'index.html', {'celulares': celulares})

def contacto(request):
    return render(request, 'vistas/Form.html')

def catalogo_view(request):
    celulares = Celular.objects.all()
    if request.method == 'POST':
        form = AñadirAlCarritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = AñadirAlCarritoForm()
    context = {
        'celulares': celulares,
        'form': form
    }
    return render(request, 'vistas/catalogo.html', context)

def carrito_view(request):
    carrito = Carrito.objects.all()
    return render(request, 'vistas/carrito.html', {'carrito': carrito})

def agregar_al_carrito(request, celular_id):
    celular = get_object_or_404(Celular, id=celular_id)
    carrito_item, created = Carrito.objects.get_or_create(celular=celular)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('catalogo')
