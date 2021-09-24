
# celery 加參數的方法
for x in range(MAX_UPLOAD_TO_TENCENT_TASK_INT):
    CELERYBEAT_SCHEDULE['upload_to_tencent_' + str(x)] = {
        'task': 'avnight.tasks.cloudfront_file_to_tencent_within_cerlery',
        'schedule': crontab(minute='*'),
        'args': [x],
    }
