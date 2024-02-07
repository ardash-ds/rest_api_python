from django.urls import path

from ..views import add_post, block_subscription, get_list_posts
    

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
    path(
        route="get_list_posts/",
        view=get_list_posts,
        name="get_list_posts",
    ),
]
