from rest_framework import serializers
from web.models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id_categoria','nombre_categoria']
        
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','descripcion','precio','categoria','imagen']
