from django.contrib import admin
from .models import Ciudad, Perfil, Usuario, Categoria, Producto

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
