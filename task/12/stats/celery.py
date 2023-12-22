from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stats.settings')

# Create a Celery instance and configure it.
app = Celery('stats')

app.conf.beat_schedule = {
    'add-random-status-every-hour': {
        'task': 'status_app.tasks.add_random_status',
        'schedule': crontab(minute=0, hour='*'),
    },
}

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps.
app.autodiscover_tasks()
