from rest_framework import serializers
from .models import Artista, Evento


class EventoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'tipo', 'fecha', 'lugar', 'descripcion', 'activo']


class ArtistaSerializer(serializers.ModelSerializer):
    eventos = EventoSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Artista
        fields = '__all__'


class ArtistaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['id', 'nombre_artistico']


class EventoReadSerializer(serializers.ModelSerializer):
    artista = ArtistaSimpleSerializer(read_only=True)

    class Meta:
        model = Evento
        fields = '__all__'


class EventoWriteSerializer(serializers.ModelSerializer):
    artista = serializers.PrimaryKeyRelatedField(
        queryset=Artista.objects.all()
    )

    class Meta:
        model = Evento
        fields = '__all__'