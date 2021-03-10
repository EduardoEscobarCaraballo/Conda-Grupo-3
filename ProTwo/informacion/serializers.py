from rest_framework import serializers
from informacion.models import informacion
from configuracion.serializers import ConfiguracionSerializer


class InformacionSerializer(serializer.Serializer):
    id_usuario_var = ConfiguracionSerializer()
    descripcion_var = serializers.CharField(max_length=128)
    fotoperfil_var = serializers.ImageField(upload_to='imagen')

    class Meta:
        model = informacion
        fields = ['id_usuario_var', 'descripcion_var', 'fotoperfil_var']

    def create(self, validated_data):
        return informacion.objets.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_usuario_var = validated_data.get('id_usuario_var', id_usuario_var)
        instance.descripcion_var = validated_data.get('descripcion_var', instance.descripcion_var)
        instance.fotoperfil_var = validated_data.get('fotoperfil_var', instance.fotoperfil_var)
        instance.save()
        return instance