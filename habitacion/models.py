from django.db import models
from .choices import estado, tipoHabitación

# Create your models here.
class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    piso = models.CharField(max_length=3)
    description = models.TextField(null=True, blank=True)
    caracteristicas = models.TextField(null=True, blank=True)
    precio_diario = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=15, choices=estado, default='Libre')
    tipo_habitación = models.CharField(max_length=20, choices=tipoHabitación, default='Individual')

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'

