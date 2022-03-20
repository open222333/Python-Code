from celery import Celery
from celery.schedules import crontab

app = Celery()
@app.on_after_configure.connect
def setup_peridoic_tasks(sender, **kwargs):
    sender.add_per