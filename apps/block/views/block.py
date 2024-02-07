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
    get_list_posts_core,
)
from ..serializers import (
    BlockUserRequestSerializer,
    GetListPostsResponseSerialiser,
    PostRequestSerializer, 
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
    request=BlockUserRequestSerializer,
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


@extend_schema(
    summary="WORKS: Get list of posts",
    description="Get a list of posts to which the user is subscribed.",
    methods=["GET"],
    responses={
        200: OpenApiResponse(response=GetListPostsResponseSerialiser),
        400: OpenApiResponse(description="Error: Bad request"),
        401: OpenApiResponse(description="Error: Unauthorized"),
        404: OpenApiResponse(description="Error: Not found"),
        409: OpenApiResponse(description="Error: You are already subscribed"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_list_posts(request: HttpRequest) -> HttpResponse:
    response = get_list_posts_core(request=request)
    return Response(response.data, status=status.HTTP_200_OK)
