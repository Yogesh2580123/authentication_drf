from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    create_by = serializers.CharField(read_only=True, source="create_by.username")
    role = serializers.CharField(read_only=True, source="create_by.role")
    class Meta:
        model = Post
        fields = ["title", "content", "create_by", "role"]
        read_only_fields = ["create_by", "role"]