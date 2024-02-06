from rest_framework.parsers import JSONParser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from django.db import transaction
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404

from ..serializers import UserRegistrationRequestSerializer
from ..models import UserModel


@transaction.atomic
def sign_up_core(request: HttpRequest) -> None:
    data = JSONParser().parse(request)
    serializer = UserRegistrationRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    UserModel.objects.create_user(
        username=serializer.validated_data["username"], 
        password=serializer.validated_data["password"], 

    )
    