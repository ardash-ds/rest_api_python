from rest_framework import serializers
from ..models import UserModel


class UserRegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'email', 
            'password',
        ]
        