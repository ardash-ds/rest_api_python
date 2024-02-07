from django.urls import path

from ..views import add_post, block_subscription
    

urlpatterns = [
    path(
        route="add_post/",
        view=add_post,
        name="add_post",
    ),
    path(
        route="block_subscription/",
        view=block_subscription,
        name="block_subscription",
    ),
]
