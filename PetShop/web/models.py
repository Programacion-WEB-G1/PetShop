from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Usuario(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name='run')
    username = models.CharField(max_length=10, verbose_name='username')
    nombres = models.CharField(max_length=60,verbose_name='nombres')
    apellidos = models.CharField(max_length=60,verbose_name='apellidos')
    password = models.CharField(max_length=255,verbose_name='password')
    perfil = models.IntegerField(null=True,blank=True,verbose_name='perfil')
