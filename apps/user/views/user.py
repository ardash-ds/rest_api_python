from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, HttpRequest

from ..core import sign_up_core
from ..serializers import UserRegistrationRequestSerializer


@extend_schema(
    summary="WORKS: Sign-up by email and password",
    description="Take email and password, create user",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
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
@api_view(["POST"])
@permission_classes([AllowAny])
def sign_up(request: HttpRequest) -> HttpResponse:
    sign_up_core(request=request)
    return HttpResponse(status=201)
