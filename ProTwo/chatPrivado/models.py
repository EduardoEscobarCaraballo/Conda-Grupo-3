from django.db import models
from configuracion.models import Configuracion

# Create your models here.
class Mensaje(models.Model):
        mensaje = models.CharField(max_length=128)
        id_usuario = models.ForeignKey(Configuracion, on_delete=models.CASCADE)
        fecha = models.DateField()

class chatPrivado(models.Model):
        id_usuario_var = models.ForeignKey(Configuracion, on_delete=models.CASCADE)
        mensaje_var = models.ForeignKey(Mensaje, on_delete=models.CASCADE)