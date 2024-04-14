from django.db import models
from django.core.validators import EmailValidator

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='usuarios')
    correo = models.EmailField(validators=[EmailValidator])
    clave = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.nombre

class Venta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ventas')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas')
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField(auto_now_add=True)

    def _str_(self):
        return f"{self.usuario} - {self.producto}"
    