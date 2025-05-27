from django.db import models

# Create your models here.

class Preregistro(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    ci = models.CharField(max_length=20, verbose_name='Carnet de Identidad')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"
