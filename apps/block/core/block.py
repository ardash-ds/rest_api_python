from rest_framework.parsers import JSONParser
from rest_framework.exceptions import APIException

from django.db import transaction
from django.http import HttpRequest

from ...user.models import UserModel
from ..serializers import (
    BlockUserRequestSerializer,
    GetListPostsResponseSerialiser,
    PostRequestSerializer, 
)
from ..models import BlockModel, BlockUserModel, PostUserModel


@transaction.atomic
def add_post_core(request: HttpRequest) -> None:
    data = JSONParser().parse(request)
    serializer = PostRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    block = BlockModel.objects.get(user_id=request.user.id)
    serializer.validated_data["block"] = block
    post = serializer.save()
    
    users = UserModel.objects.filter(block_user_for_user__block=block).values_list("id", flat=True)
    for user_id in users:
        PostUserModel.objects.create(user_id=user_id, post_id=post.id)


def block_subscription_core(request: HttpRequest) -> None:
    data = JSONParser().parse(request)
    serializer = BlockUserRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    if BlockUserModel.objects.filter(
        user=request.user,
        block=serializer.validated_data["block"],
    ).exists():
        raise APIException(detail="You are already subscribed")
    else:
        serializer.validated_data["user"] = request.user
        serializer.save()
    

def get_list_posts_core(request: HttpRequest) -> list[PostUserModel]:
    user = request.user
    posts = PostUserModel.objects.filter(user=user).select_related("post")
    return GetListPostsResponseSerialiser(posts, many=True)
    

def mark_post_read_core(request: HttpRequest) -> None:   
    post_user_id = request.GET.get("post_user_id")
    post_user = PostUserModel.objects.get(id=post_user_id)
    post_user.read_status = True
    post_user.save()
    