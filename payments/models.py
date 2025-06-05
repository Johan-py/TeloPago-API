from django.db import models

# Create your models here.
from django.db import models

class Compra(models.Model):
    usuario = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='compras')
    url_producto = models.URLField(max_length=500)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='pendiente')  # ejemplo: pendiente, procesando, completado

    def __str__(self):
        return f"Compra {self.id} de {self.usuario.email} - {self.url_producto[:30]}..."
