from celery import shared_task
from datetime import date, timedelta

from django.core.mail import send_mail

from apps.user.models import UserModel
from apps.block.models import PostUserModel


@shared_task
def sending_out_posts():
    
    for user in UserModel.objects.all():
        posts_user = PostUserModel.objects.filter(
            post__created_at__gt=date.today() - timedelta(days=1),
            user=user,
        ).select_related("post")
        if posts_user:
            user_email = user.email
            post_list = []
            for post_user in posts_user:
                post_list.append(post_user.post.title)
            send_mail(
                'Newsletter',
                ' '.join(post_list),
                'from@example.com',
                [user_email,],
                fail_silently=False,
            )
        
    