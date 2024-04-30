from django.urls import path
from . import views

urlpatterns = [
    path('producto/', views.lista_producto,name="lista_producto"),
    path('categoria/', views.lista_categoria,name="lista_categoria"),    
    path('producto/<id_producto>', views.vista_producto,name="vista_producto"),    
]