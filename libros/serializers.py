from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
        read_only_fields = ['id', 'creado_el']

    def validate_precio(self, value):
        """Validación a nivel de campo (método limpio/senior)."""
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value