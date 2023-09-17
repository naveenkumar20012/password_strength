# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'password_checker.settings')

app = Celery('password_checker')  # Replace 'myprojj' with your project's name.
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

# Load task modules from all registered Django app configs.
app.config_from_object(settings, namespace='CELERY')

# Auto-discover tasks in all installed applications.
# Using Redis as the message broker
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {self.request!r}')
