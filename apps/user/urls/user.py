from django.urls import path, include

from ..views import sign_up
    

urlpatterns = [
    path(
        route='sign_up/',
        view=sign_up,
        name='sign_up',
    ),
]
