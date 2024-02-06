import json

from rest_framework.parsers import JSONParser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404

from ..serializers import PostRequestSerializer
from ..models import PostModel, BlockModel


@transaction.atomic
def add_post_core(request: HttpRequest) -> None:
    data = JSONParser().parse(request)
    serializer = PostRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    block = BlockModel.objects.get(user_id=request.user.id)
    serializer.validated_data["block"] = block
    serializer.save()
