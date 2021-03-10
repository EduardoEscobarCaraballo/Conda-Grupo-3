from django.db import models

# Create your models here.

class Configuracion(models.Model):
        nombre_var = models.CharField(max_length=128)
        id_usuario_var = models.CharField(max_length=128, unique=True, primary_key=True)
        email_var = models.CharField(max_length=128)
        web_var = models.CharField(max_length=128)
        telefono_var = models.CharField(max_length=128)
        sexo_var = models.CharField(max_length=128)
        fotoperfil_var = models.ImageField(upload_to='imagen')