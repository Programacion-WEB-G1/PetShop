from django.contrib import admin
from .models import Ciudad, Usuario, Producto, Venta

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Venta)
