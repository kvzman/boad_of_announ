import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boa_project.settings')

app = Celery('boa_project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
