from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse, HttpRequest

from ..core import sign_up_core, sign_in_core, get_user_core
from ..serializers import (
    UserRegistrationRequestSerializer, 
    GetUserResponseSerializer,
)
from ..services import get_token_http_response


@extend_schema(
    summary="WORKS: Sign-up by username and password",
    description="Take username and password, create user",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        400: OpenApiResponse(description="Error: Bad request"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "user",
    ],
)
@api_view(["POST"])
@permission_classes([AllowAny])
def sign_up(request: HttpRequest) -> HttpResponse:
    sign_up_core(request=request)
    return HttpResponse(status=200)


@extend_schema(
    summary="WORKS: Sign-in by username and password",
    description="Take user's username and password and return 'access' and 'refresh' tokens",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "user",
    ],
)
@api_view(['POST'])
@permission_classes([AllowAny])
def sign_in(request: HttpRequest) -> HttpResponse:
    user = sign_in_core(request=request)
    return get_token_http_response(user)


@extend_schema(
    summary="WORKS: Gets the username of the authorized user",
    methods=["GET"],
    responses={
        201: OpenApiResponse(description="Successfully registrated."),
        400: OpenApiResponse(description="Error: Bad request"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "user",
    ],
)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_user(request: HttpRequest) -> HttpResponse:
    response = get_user_core(request=request)
    return Response(response.data, status=status.HTTP_200_OK)
