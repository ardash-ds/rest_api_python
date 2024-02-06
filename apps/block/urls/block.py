from django.urls import path

from ..views import add_post
    

urlpatterns = [
        path(
        route='add_post/',
        view=add_post,
        name='add_post',
    ),
]
