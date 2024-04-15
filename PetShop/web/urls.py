from django.urls import path
from .views import index, gato, perro, carro, producto, perfil, recupera, user, base

urlpatterns = [
    path('', index, name="index"),
    path('gato/', gato),
    path('carro/', carro),
    path('producto/', producto),
    path('perro/', perro),
    path('recupera/', recupera),
    path('perfil/', perfil),
    path('user/', user),
    path('base/', base),
]