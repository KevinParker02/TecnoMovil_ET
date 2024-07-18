from django.db import models

class Categoria(models.Model):
    marca = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marca

class Celular(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    description = models.TextField()
    imagen = models.ImageField(upload_to='celulares/', blank=True, null=True)
    marca = models.ManyToManyField(Categoria)
    stock = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Celulares"
    def str(self):
        return self.nombre

class Blog(models.Model):
    imagen = models.ImageField(upload_to='blogs/', blank=True, null=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
    
#Carrito#

class Carrito(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.cantidad * self.celular.precio
