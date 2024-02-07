from rest_framework import serializers

from ..models import PostModel, BlockUserModel, PostUserModel


class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["title", "description"]
        read_only_fields = ["block", "created_at",]
        
        
class BlockUserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockUserModel
        fields = ["block"]
        read_only_fields = ["user"]
        
class GetListPostsResponseSerialiser(serializers.ModelSerializer):
    title = serializers.CharField(source='post.title', read_only=True)
    
    class Meta:
        model = PostUserModel
        fields = ["id", "read_status", "title"]
    
    