from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
    
    
def get_token_http_response(user, refresh_token: str = None) -> HttpResponse:
    """Generates and returns an HTTP response that includes the access and refresh tokens for the given user.

    Arguments:
    - user: A UserModel object representing the user to generate tokens for.
    - refresh_token: user's 'refresh' token. If provided, generates a new 'access' token for user.

    Return:
    - An HttpResponse object with cookies set for access and refresh tokens.
    """

    http_response = HttpResponse(status=200)
    if refresh_token:
        token = RefreshToken(token=refresh_token)
    else:
        token = RefreshToken.for_user(user)
        http_response.set_cookie("refresh", str(token), httponly=True)
    http_response.set_cookie("access", str(token.access_token), httponly=True)
    return http_response