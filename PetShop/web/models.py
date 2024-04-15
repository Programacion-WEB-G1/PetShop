from pyexpat import model
from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_ciudad

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    correo = models.EmailField()
    clave = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre