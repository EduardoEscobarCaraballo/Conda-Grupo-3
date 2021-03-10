from rest_framework import serializers
from registro.models import registro
from configuracion.serializers import ConfiguracionSerializer


class RegistroSerializer(serializer.Serializer):
    id_usuario_var = ConfiguracionSerializer()
    contraseña_var = serializers.CharField(max_length=128)

    class Meta:
        model = registro
        fields = ['id_usuario_var', 'contraseña_var']

    def create(self, validated_data):
        return registro.objets.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_usuario_var = validated_data.get('id_usuario_var', id_usuario_var)
        instance.contraseña_var = validated_data.get('contraseña_var', instance.contraseña_var)
        instance.save()
        return instance