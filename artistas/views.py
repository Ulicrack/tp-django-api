from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Artista
from .serializers import ArtistaSerializer


@api_view(['GET', 'POST'])
def lista_artistas(request):

    if request.method == 'GET':
        artistas = Artista.objects.all()
        serializer = ArtistaSerializer(artistas, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_artista(request, pk):

    try:
        artista = Artista.objects.get(pk=pk)
    except Artista.DoesNotExist:
        return Response(
            {'error': 'Artista no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ArtistaSerializer(artista)

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistaSerializer(
            artista,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        artista.delete()

        return Response(
            {'mensaje': 'Artista eliminado correctamente'},
            status=status.HTTP_204_NO_CONTENT
        )