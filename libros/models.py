from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    sinopsis = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    publicado = models.BooleanField(default=True)
    creado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_el']

    def __str__(self):
        return f"{self.titulo} - {self.autor}"