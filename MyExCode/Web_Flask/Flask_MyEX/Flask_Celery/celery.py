from celery import Celery
from app import app
import os

app.config['CELERY_BROKER_URL'] = os.environ.get('CELERY_BROKER_URL')
# CELERY_RESULT_BACKEND 選項只有在你必須要 Celery 任務的存儲狀態和運行結果的時候才是必須的。
app.config['CELERY_RESULT_BACKEND'] = os.environ.get('CELERY_RESULT_BACKEND')


celery = Celery(
    app.name,
    broker=app.config['CELERY_BROKER_URL']
)
celery.conf.update(app.config)
TaskBase = celery.Task


class ContextTask(TaskBase):
    # if set the component will not be registered, but can be used as a component base class.
    abstract = True

    def __call__(self, *args, **kwds):
        return TaskBase.__call__(self, *args, **kwds)


# https://stackoverflow.com/questions/53726215/what-is-the-purpose-of-celerys-autodiscover-tasks-function
# celery.autodiscover_tasks(
#     [app.name] + list(app.blueprints.keys()), related_name='tasks'
# )
celery.Task = ContextTask
task = celery.task
