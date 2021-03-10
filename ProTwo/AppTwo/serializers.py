from rest_framework import serializers
from AppTwo.models import Post
from configuracion.serializers import ConfiguracionSerializer


class PostSerializer(serializer.Serializer):
    index_var = serializers.CharField(max_length=128)
    comment_var = serializers.CharField(max_length=128)
    id_usuario_var = ConfiguracionSerializer()
    likes_var = serializers.CharField(max_length=128)
    caption_var = serializers.CharField(max_length=128)
    foto_post_var = serializers.ImageField(upload_to='post')

    class Meta:
        model = Post
        fields = ['index_var', 'comment_var', 'id_usuario_var', 'likes_var', 'caption_var', 'foto_post_var']
        
    def create(self, validated_data):
        return Post.objets.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.index_var = validated_data.get('index_var', instance.index_var)
        instance.comment_var = validated_data.get('comment_var', instance.comment_var)
        instance.id_usuario_var = validated_data.get('id_usuario_var', id_usuario_var)
        instance.likes_var = validated_data.get('likes_var', instance.likes_var)
        instance.caption_var = validated_data.get('caption_var', instance.caption_var)
        instance.foto_post_var = validated_data.get('foto_post_var', instance.foto_post_var)
        instance.save() 
        return instance