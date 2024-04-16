from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True, verbose_name='id_ciudad')
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Ciudad')

    def _str_(self):
        return self.nombre

class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True, verbose_name='id_perfil')
    perfil = models.CharField(max_length=100, null=True, verbose_name='perfil')

    def _str_(self):
        return self.perfil

class Usuario(models.Model):
    run = models.CharField(primary_key=True,max_length=11, verbose_name='run',default='00000000-0', unique=True)
    nombres = models.CharField(max_length=60,verbose_name='nombres')
    apellidos = models.CharField(max_length=60,verbose_name='apellidos')
    username = models.CharField(max_length=10, verbose_name='username')
    email = models.EmailField(validators=[EmailValidator],verbose_name='email', null=True)
    password = models.CharField(max_length=255,verbose_name='password')
    fechanac = models.DateField(null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='Usuarios', null=True)
    direccion = models.CharField(max_length=100,verbose_name='direccion', null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Usuario', default='2', null=True)

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='Id de la categoria')
    nombre_categoria = models.CharField(max_length=60,verbose_name='categoria')

    def __str__(self):
        return self.nombre_categoria
    
class Producto(models.Model):
    id_producto = models.CharField(max_length=20, primary_key=True, verbose_name='id_producto')
    nombre = models.CharField(max_length=100, verbose_name='Nombre del producto', null=True)
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name='Imagen del producto')

    def __str__(self):
        return self.nombre
