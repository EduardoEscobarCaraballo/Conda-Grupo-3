from django.db import models
from configuracion.models import Configuracion


# Create your models here.

class Post(models.Model):
        index_var = models.CharField(max_length=128, unique=True)
        comment_var = models.CharField(max_length=128)
        id_usuario_var = models.ForeignKey(Configuracion, on_delete=models.CASCADE)
        likes_var = models.CharField(max_length=128)
        caption_var = models.CharField(max_length=128)
        foto_post_var = models.ImageField(upload_to='post')