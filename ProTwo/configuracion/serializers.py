from rest_framework import serializers
from configuracion.models import Configuracion


class ConfiguracionSerializer(serializer.Serializer):
    nombre_var = serializers.CharField(max_length=128)
    id_usuario_var = serializers.CharField(max_length=128)
    email_var = serializers.CharField(max_length=128)
    web_var = serializers.CharField(max_length=128)
    telefono_var = serializers.CharField(max_length=128)
    sexo_var = serializers.CharField(max_length=128)
    fotoperfil_var = serializers.ImageField(upload_to='imagen')

    class Meta:
        model = Configuracion
        fields = ['nombre_var', 'id_usuario_var', 'email_var', 'web_var', 'telefono_var', 'sexo_var', 'fotoperfil_var']
        
        
    def create(self, validated_data):
        return Configuracion.objets.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nombre_var = validated_data.get('nombre_var', instance.nombre_var)
        instance.id_usuario_var = validated_data.get('id_usuario_var', instance.id_usuario_var)
        instance.email_var = validated_data.get('email_var', instance.email_var)
        instance.web_var = validated_data.get('web_var', instance.web_var)
        instance.telefono_var = validated_data.get('telefono_var', instance.telefono_var)
        instance.sexo_var = validated_data.get('sexo_var', instance.sexo_var)
        instance.fotoperfil_var = validated_data.get('fotoperfil_var', instance.fotoperfil_var)
        instance.save() 
        return instance