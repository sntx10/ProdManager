import os
from celery import Celery
from decouple import config
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.conf.broker_url = config('CELERY_BROKER_URL')
app.conf.result_backend = config('CELERY_RESULT_BACKEND')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_connection_retry_on_startup = True

app.autodiscover_tasks()
