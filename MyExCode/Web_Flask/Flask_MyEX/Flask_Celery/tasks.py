from datetime import datetime
import celery


@celery.task(bind=True)
def print_datetime():
    return datetime.now().__format__('%Y-%m-%d %H:%M:%S')
