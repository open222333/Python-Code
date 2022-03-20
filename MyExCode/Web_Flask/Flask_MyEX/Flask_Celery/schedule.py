import os
from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {}

if os.environ.get('PRINT_DATETIME'):
    CELERYBEAT_SCHEDULE['print_datetime'] = {
        'task': 'tasks.print_datetime',
        'schedule': crontab(minute='*')
    }
