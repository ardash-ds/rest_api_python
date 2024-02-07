from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.http import HttpRequest, HttpResponse

from ..core import (
    add_post_core,
    block_subscription_core,
)
from ..serializers import (
    GetListPostsResponseSerialiser,
    PostRequestSerializer, 
    SubscriptionRequestSerializer,
)


@extend_schema(
    summary="WORKS: Create post",
    description="Take post title and description, create a new post.",
    request=PostRequestSerializer,
    methods=["POST"],
    responses={
        201: OpenApiResponse(description="Post successfully created"),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_post(request: HttpRequest) -> HttpResponse:
    response = add_post_core(request=request)
    return Response(response, status=status.HTTP_201_CREATED)


@extend_schema(
    summary="WORKS: Block subscription",
    description="Take the block ID and subscribe to it.",
    request=SubscriptionRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Subscription completed"),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def block_subscription(request: HttpRequest) -> HttpResponse:
    block_subscription_core(request=request)
    return HttpResponse(status=200)
