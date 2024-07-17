from django.db import models

class Categoria(models.Model):
    marca = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.marca

class Celular(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='celulares/', blank=True, null=True)
    marca = models.ManyToManyField(Categoria)
    tienda = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.celular.nombre}'