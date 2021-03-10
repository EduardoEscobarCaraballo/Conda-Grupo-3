from django.db import models
from configuracion.models import Configuracion


# Create your models here.

class registro(models.Model):
        id_usuario_var = models.ForeignKey(Configuracion, on_delete=models.CASCADE)
        contraseña_var = models.CharField(max_length=128)