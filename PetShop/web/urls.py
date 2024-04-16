from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, carro, producto, perfil, recupera, user, base, cerrar_sesion, productos_perro, productos_gato

urlpatterns = [
    path('', index, name="index"),
    path('gato/', productos_gato, name='productos_gato'),
    path('carro/', carro),
    path('producto/', producto, name="productos"),
    path('perro/', productos_perro, name='productos_perro'),
    path('recupera/', recupera),
    path('perfil/', perfil),
    path('user/', user, name="user"),
    path('base/', base),
    path('cerrar-sesion/', cerrar_sesion, name="cerrar_sesion"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)