import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
 
app = Celery('config')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending_posts_every_day': {
        'task': 'core.tasks.tasks.sending_out_posts',
        'schedule': crontab(minute=0, hour=0),
    },
}
