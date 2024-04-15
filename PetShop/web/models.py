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
    run = models.IntegerField(primary_key=True, verbose_name='run', unique=True)
    nombres = models.CharField(max_length=60,verbose_name='nombres')
    apellidos = models.CharField(max_length=60,verbose_name='apellidos')
    username = models.CharField(max_length=10, verbose_name='username')
    email = models.EmailField(validators=[EmailValidator],verbose_name='email', null=True)
    password = models.CharField(max_length=255,verbose_name='password')
    fechanac = models.DateField(null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='Usuarios', null=True)
    direccion = models.CharField(max_length=100,verbose_name='direccion', null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Usuario', null=True)
