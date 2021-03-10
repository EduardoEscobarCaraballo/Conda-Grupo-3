from rest_framework import serializers
from publicacion.models import publicacion
from configuracion.serializers import ConfiguracionSerializer


class PublicacionSerializer(serializer.Serializer):
    id_usuario_var = ConfiguracionSerializer()
    imagenid_var = serializers.CharField(max_length=128)
    caption_var = serializers.CharField(max_length=128)
    fotoperfil_var = serializers.ImageField(upload_to='imagen')

    class Meta:
        model = publicacion
        fields = ['id_usuario_var', 'imagenid_var', 'caption_var', 'fotoperfil_var']

    def create(self, validated_data):
        return publicacion.objets.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_usuario_var = validated_data.get('id_usuario_var', id_usuario_var)
        instance.imagenid_var = validated_data.get('imagenid_var', instance.imagenid_var)
        instance.caption_var = validated_data.get('caption_var', instance.caption_var)
        instance.fotoperfil_var = validated_data.get('fotoperfil_var', instance.fotoperfil_var)
        instance.save()
        return instance