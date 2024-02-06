from rest_framework import serializers

from ..models import PostModel


class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['title', 'description']
        read_only_fields = ["block", 'created_at',]