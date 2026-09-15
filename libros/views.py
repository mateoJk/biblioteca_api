from rest_framework import generics
from .models import Libro, Categoria
from .serializers import LibroSerializer, CategoriaSerializer


# VISTAS PARA CATEGORIAS


class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    """GET: Lista categorías | POST: Crea una categoría"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET / PUT / DELETE de una categoría por ID"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# VISTAS PARA LIBROS

class LibroListCreateAPIView(generics.ListCreateAPIView):
    """GET: Lista libros | POST: Crea un libro"""
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LibroDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET / PUT / DELETE de un libro por ID"""
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer