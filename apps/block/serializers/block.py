from rest_framework import serializers

from ..models import PostModel, BlockUserModel, PostUserModel


class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["title", "description"]
        read_only_fields = ["block", "created_at",]
        
        
class SubscriptionRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    

class GetListPostsResponseSerialiser(serializers.ModelSerializer):
#     post = serializers.CharField(sourse="post_user_for_post__title")
#     read_status = serializers.BooleanField()
    
    class Meta:
        model = PostUserModel
        fields = ["post", "read_status"]
    
    