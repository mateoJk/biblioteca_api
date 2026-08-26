from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Libro
from .serializers import LibroSerializer

@api_view(['GET', 'POST'])
def libro_list_create_api_view(request):
    """
    GET: Lista todos los libros.
    POST: Crea un nuevo libro.
    """
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def libro_detail_api_view(request, pk):
    """
    GET: Recupera un libro por ID.
    PUT: Actualiza un libro por ID.
    DELETE: Elimina un libro por ID.
    """
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        libro.delete()
        return Response(
            {"message": "Libro eliminado correctamente"}, 
            status=status.HTTP_204_NO_CONTENT
        )