from rest_framework import serializers
from cabecera.models import Cabecera
from configuracion.serializers import ConfiguracionSerializer


class CabeceraSerializer(serializer.Serializer):
    id_usuario_var = ConfiguracionSerializer()
    historia_var = serializers.CharField(max_length=128)
    visualizaciones_var = serializers.CharField(max_length=128)

    class Meta:
        model = Cabecera
        fields = ['id_usuario_var', 'historia_var', 'visualizaciones_var']

    def create(self, validated_data):
        return Cabecera.objets.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id_usuario_var = validated_data.get('id_usuario_var', id_usuario_var)
        instance.historia_var = validated_data.get('historia_var', instance.historia_var)
        instance.visualizaciones_var = validated_data.get('visualizaciones_var', instance.visualizaciones_var)
        instance.save()
        return instance