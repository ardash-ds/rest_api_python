from django.conf import settings
from drf_spectacular.authentication import OpenApiAuthenticationExtension
from rest_framework.permissions import IsAuthenticated as _IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken


class IsAuthenticated(_IsAuthenticated):
    """Custom permission class that checks whether the request has a valid authentication token.

    Inherits from _IsAuthenticated, which is a Django Rest Framework class that checks for authentication based
    on whether the user making the request is authenticated or not.

    Overrides the has_permission() method to check whether the request authorization token is present and not None.

    Args:
        _IsAuthenticated: A class provided by Django Rest Framework which checks if the user making the request is
        authenticated or not.

    Returns:
        bool: True if the request has a valid authentication token else False.
    """

    def has_permission(self, request, view) -> bool:
        return request.auth is not None


class CookiesAuthentication(JWTAuthentication):
    """Custom authentication class for Django REST Framework that authenticates users using JSON Web Tokens (JWTs)
    stored in cookies.

    Attributes:
        None.

    Methods:
        authenticate(request):
            Authenticates the user based on the JWT stored in the REST_FRAMEWORK['JWT_AUTH_COOKIE'] cookie.
            If the token is not present in the cookie, returns None.
            If the token is present and valid, returns a tuple of the user identified by the token and the token itself.

    Usage:
        - Add 'django.contrib.sessions.middleware.SessionMiddleware' and 'django.contrib.auth.middleware.AuthenticationMiddleware'
          to MIDDLEWARE in settings.py
        - Add the following settings to settings.py:
            REST_FRAMEWORK = {
                'DEFAULT_AUTHENTICATION_CLASSES': (
                    'path.to.CookiesAuthentication',
                    ...
                ),
                'JWT_AUTH_COOKIE': 'jwt',
                ...
            }
    """

    def authenticate(self, request):
        token = request.COOKIES.get(settings.REST_FRAMEWORK["JWT_AUTH_COOKIE"])
        if token is not None:
            return self.get_user_token_pair(token)
        return None, None

    def get_user_token_pair(self, token):
        try:
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
            return user, validated_token
        except (InvalidToken, AuthenticationFailed):
            return None, None


class CookiesAuthenticationExtension(OpenApiAuthenticationExtension):
    """OpenAPI specification extension for Swagger UI and ReDoc to document the cookie-based authentication using
    'access' token.

    Attributes:
        target_class (class): The authentication class that needs to be documented.
        name (str): The name of the authentication class.

    Methods:
        get_authenticator():
            Returns an instance of the target_class.

        get_security_definition(auto_schema):
            Returns the security definition for the target_class.

    Usage:
        - Import the necessary packages and the class.
        - Instantiate the class and pass the target_class and name as parameters.
        - Use the get_authenticator() method to get an instance of the target_class.
        - Use the get_security_definition(auto_schema) method to get the security definition dictionary.
    """

    target_class = CookiesAuthentication
    name = "Authorization"

    def get_authenticator(self):
        return self.target_class()

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "in": "cookies",
            "name": "Authorization",
            "description": "Cookie-based authentication by 'access' token",
        }
