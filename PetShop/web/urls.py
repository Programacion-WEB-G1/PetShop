from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, carro, producto, miperfil, recupera, user, base, cerrar_sesion, productos_perro, productos_gato, agregar_al_carrito, api_pet, reset_password, api_pet2

urlpatterns = [
    path('', index, name="index"),
    path('gato/', productos_gato, name='productos_gato'),
    path('carro/', carro),
    path('producto/', producto, name="productos"),
    path('perro/', productos_perro, name='productos_perro'),
    path('recupera/', recupera),
    path('perfil/', miperfil),
    path('user/', user, name="user"),
    path('base/', base),
    path('cerrar-sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('agregar-al-carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('api-pet/', api_pet, name="api_pet"),
    path('recupera/', reset_password, name="reset"),
    path('api-pet2/', api_pet2, name="api_pet2"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)