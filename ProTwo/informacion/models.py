from django.db import models
from configuracion.models import Configuracion


# Create your models here.

class informacion(models.Model):
        id_usuario_var = models.ForeignKey(Configuracion, on_delete=models.CASCADE)
        descripcion_var = models.CharField(max_length=128)
        fotoperfil_var = models.ImageField(upload_to='imagen')