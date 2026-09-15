from django.urls import path
from . import views

urlpatterns = [
    # URLs de Categorías
    path('categorias/', views.CategoriaListCreateAPIView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', views.CategoriaDetailAPIView.as_view(), name='categoria-detail'),

    # URLs de Libros
    path('libros/', views.LibroListCreateAPIView.as_view(), name='libro-list-create'),
    path('libros/<int:pk>/', views.LibroDetailAPIView.as_view(), name='libro-detail'),
]