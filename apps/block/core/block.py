from rest_framework.parsers import JSONParser

from django.db import transaction
from django.http import HttpRequest

from ..serializers import PostRequestSerializer, SubscriptionRequestSerializer
from ..models import BlockModel, BlockUserModel, PostUserModel


@transaction.atomic
def add_post_core(request: HttpRequest) -> None:
    data = JSONParser().parse(request)
    serializer = PostRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    block = BlockModel.objects.get(user_id=request.user.id)
    serializer.validated_data["block"] = block
    post = serializer.save()
    
    users = BlockUserModel.objects.filter(block=block).values_list("id", flat=True)
    for user_id in users:
        PostUserModel.objects.create(user_id=user_id, post_id=post.id)


def block_subscription_core(request: HttpRequest) -> None:
    data = JSONParser().parse(request)
    serializer = SubscriptionRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.validated_data["id"], 
    BlockUserModel.objects.create(
        user_id=request.user.id,
        block_id=serializer.validated_data["id"]
    )
    
    

    
    