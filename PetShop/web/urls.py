from django.urls import path
from .views import index, gato, perro, carro, producto, perfil, recupera, user, base, cerrar_sesion

urlpatterns = [
    path('', index, name="index"),
    path('gato/', gato),
    path('carro/', carro),
    path('producto/', producto, name="productos"),
    path('perro/', perro),
    path('recupera/', recupera),
    path('perfil/', perfil),
    path('user/', user, name="user"),
    path('base/', base),
    path('cerrar-sesion/', cerrar_sesion, name="cerrar_sesion"),
]