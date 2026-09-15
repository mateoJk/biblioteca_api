from rest_framework import serializers
from .models import Libro, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)

    class Meta:
            model = Libro
            fields = [
                'id', 'titulo', 'autor', 'sinopsis', 
                'precio', 'publicado', 'categoria', 
                'categoria_detalle', 'creado_el'
            ]
            read_only_fields = ['id', 'creado_el']

    def validate_precio(self, value):
        """Validacion a nivel de campo"""
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value