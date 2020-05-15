from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'test-celery': {
        'task': 'tasks.req_url',
        # Every minute
        'schedule': 10.0,
    }
}