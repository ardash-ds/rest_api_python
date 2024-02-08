from celery import shared_task
import time

from apps.user.models import UserModel


@shared_task
def sending_out_posts():
    
    time.sleep(2)
    print("sending out posts")
    