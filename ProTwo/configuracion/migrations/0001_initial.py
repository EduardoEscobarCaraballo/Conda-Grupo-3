# Generated by Django 2.2.5 on 2021-03-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('nombre_var', models.CharField(max_length=128)),
                ('id_usuario_var', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('email_var', models.CharField(max_length=128)),
                ('web_var', models.CharField(max_length=128)),
                ('telefono_var', models.CharField(max_length=128)),
                ('sexo_var', models.CharField(max_length=128)),
                ('fotoperfil_var', models.ImageField(upload_to='imagen')),
            ],
        ),
    ]
