from django.urls import path

from ..views import sign_up, sign_in, get_user
    

urlpatterns = [
    path(
        route='sign_up/',
        view=sign_up,
        name='sign_up',
    ),
    path(
        route='sign_in/',
        view=sign_in,
        name='sign_in',
    ),
    path(
        route='get_user/',
        view=get_user,
        name='get_user',
    ),
]
