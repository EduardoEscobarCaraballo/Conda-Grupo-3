from rest_framework import serializers
from chatPrivado.models import Mensaje, chatPrivado
from configuracion.serializers import ConfiguracionSerializer


class MensajeSerializer(serializer.Serializer):
    mensaje = serializers.CharField(max_length=128)
    id_usuario = ConfiguracionSerializer()
    fecha = serializers.CharField(max_length=128)
    
    class Meta:
        model = Mensaje
        fields = ['mensaje', 'id_usuario', 'fecha']
        
    def create(self, validated_data):
        return Mensaje.objets.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.mensaje = validated_data.get('mensaje', instance.mensaje)
        instance.id_usuario = validated_data.get('id_usuario', instance.comment_var)
        instance.id_usuario_var = validated_data.get('id_usuario_var', instance.fecha)
        instance.save()
        return instance
    
    
class ChatPrivadoSerializer(serializer.Serializer):
    id_usuario_var = ConfiguracionSerializer()
    mensaje_var = MensajeSerializer()
    
    class Meta:
        model = chatPrivado
        fields = ['id_usuario_var', 'mensaje_var']
        
    def create(self, validated_data):
        return chatPrivado.objets.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.id_usuario_var = validated_data.get('id_usuario_var', instance.id_usuario_var)
        instance.mensaje_var = validated_data.get('mensaje_var', instance.mensaje_var)
        instance.save() 
        return instance
    