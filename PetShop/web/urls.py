from django.urls import path
from .views import index, gato, perro, carro, iniciar, perfil, recupera, user

urlpatterns = [
    path('', index),
    path('gato/', gato),
    path('carro/', carro),
    path('iniciar/', iniciar),
    path('perro/', perro),
    path('recupera/', recupera),
    path('perfil/', perfil),
    path('user/', user),
]