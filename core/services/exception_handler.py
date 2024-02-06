from django.conf import settings
from rest_framework import exceptions, views
from rest_framework.exceptions import PermissionDenied

from core.services.auth_config import CookiesAuthentication


def custom_exceptions_handler(exc, context):
    """Custom exception handler for API responses.

    This function provides a custom handling mechanism for exceptions that occur during
    API requests. It leverages the default Django Rest Framework (DRF) exception handling,
    modifies responses where necessary, and ensures proper handling of authentication
    related exceptions.

    Args:
        exc (Exception): The exception that was raised during the API request.
        context (dict): The context of the API request.

    Returns:
        Response: A modified response object reflecting the appropriate exception status
        and detail, with additional handling for authentication exceptions.
    """

    response = views.exception_handler(exc, context)
    token = context["request"].COOKIES.get(settings.REST_FRAMEWORK["JWT_AUTH_COOKIE"])
    user, _ = CookiesAuthentication().get_user_token_pair(token=token)
    if user is None:
        # manage the case of default DRF 403 PermissionDenied
        if isinstance(exc, PermissionDenied):
            exc = exceptions.NotAuthenticated()
            if token is not None:
                exc = exceptions.AuthenticationFailed()
            response.status_code = exc.status_code
            response.data["detail"] = exc.detail

    return response
