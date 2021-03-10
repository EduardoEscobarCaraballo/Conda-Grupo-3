import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

from AppTwo.models import Post
from configuracion.models import Configuracion
from cabecera.models import Cabecera
from chatPrivado.models import chatPrivado, Mensaje
from informacion.models import informacion
from login.models import Login
from publicacion.models import publicacion
from registro.models import registro
from faker import Faker



fakegen = Faker()

def populate(N=5):  
    for entry in range(N):
        fake_index_var = fakegen.name().split()
        fake_first_name = fake_index_var[0]
        fake_first_name2 = fake_index_var[0]
        fake_last_name = fake_index_var[1]
        fake_email = fakegen.email()
        fake_email2 = fakegen.email()
        fake_id = fakegen.pyint()
        fake_web = fakegen.hostname()
        fake_web2 = fakegen.hostname()
        fake_telefono = fakegen.phone_number()
        fake_telefono2 = fakegen.phone_number()
        fake_perfil = 'perfil'
        fake_sexo = 'Hombre'
        fake_sexo2 = 'Mujer'
        fake_historia = fakegen.image_url()
        fake_visualizaciones = fakegen.pyint()
        fake_id2 = fakegen.unique.pyint()
        fake_mensaje = fakegen.text(max_nb_chars=20)
        fake_fotoperfil = fakegen.image_url()
        fake_fotoperfil2 = fakegen.image_url()
        fake_imagenid = fakegen.image_url()
        fake_caption = fakegen.text(max_nb_chars=20)
        fake_descripcion = fakegen.text(max_nb_chars=50)
        fake_comment = fakegen.text(max_nb_chars=40)
        fake_likes = fakegen.pyint()
        fake_fecha = fakegen.date_between(start_date='-1d', end_date='today')
        fake_contraseña = fakegen.unique.pyint()


        configuracion = Configuracion.objects.get_or_create(nombre_var = fake_first_name, id_usuario_var = fake_id, web_var = fake_web, fotoperfil_var = fake_fotoperfil,  email_var = fake_email,telefono_var = fake_telefono, sexo_var = fake_sexo)[0]
        print("Configuracion creada")
        configuracion2 = Configuracion.objects.get_or_create(nombre_var = fake_first_name2, id_usuario_var = fake_id2, web_var = fake_web2, fotoperfil_var = fake_fotoperfil2,  email_var = fake_email2, telefono_var = fake_telefono2, sexo_var = fake_sexo2)[0]
        print("Configuracion creada")
        appTwo = Post.objects.get_or_create(index_var = fake_index_var, comment_var = fake_comment, id_usuario_var = configuracion, likes_var = fake_likes, caption_var = fake_caption, foto_post_var = fake_fotoperfil2)[0]
        print("Post creado")
        cabecera = Cabecera.objects.get_or_create(id_usuario_var = configuracion, historia_var = fake_historia, visualizaciones_var = fake_visualizaciones)[0]
        print("Cabecera creado")
        mensaje = Mensaje.objects.get_or_create(mensaje = fake_mensaje, id_usuario = configuracion, fecha = fake_fecha)[0]
        chat_Privado = chatPrivado.objects.get_or_create(id_usuario_var = configuracion2, mensaje_var = mensaje)[0]
        print("Chat privado creado")
        informaciones = informacion.objects.get_or_create(id_usuario_var = configuracion, descripcion_var = fake_descripcion, fotoperfil_var = fake_fotoperfil )[0]
        print("Informacion creado")
        login = Login.objects.get_or_create(id_usuario_var = configuracion, contraseña_var = fake_contraseña)[0]
        print("Login creado")
        publicaciones = publicacion.objects.get_or_create(id_usuario_var = configuracion, caption_var = fake_caption, imagenid_var = fake_imagenid, fotoperfil_var = fake_fotoperfil2)[0]
        print("Publicacion creado")
        registros = registro.objects.get_or_create(id_usuario_var = configuracion, contraseña_var = fake_contraseña)[0]
        print("Registro creado")


print("Rellenando base de datos")
populate(3)

print("COMPLETADO")