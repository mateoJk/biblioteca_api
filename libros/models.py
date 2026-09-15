from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    sinopsis = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    publicado = models.BooleanField(default=True)
    creado_el = models.DateTimeField(auto_now_add=True)

    # one to many 
    # on_delete=models.PROTECT evita que se borre una categoria si tiene libros asignados.
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, 
        related_name='libros',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-creado_el']

    def __str__(self):
        return f"{self.titulo} - {self.autor}"