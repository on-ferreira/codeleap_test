from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model if local database were used instead of external API.
    """
    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
