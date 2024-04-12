from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('gato/',views.gato),
    path('carro/',views.carro),
    path('iniciar/',views.iniciar),
    path('perro/',views.perro),
    path('recupera/',views.recupera),
    path('perfil/',views.perfil),
    path('user/',views.user),
]