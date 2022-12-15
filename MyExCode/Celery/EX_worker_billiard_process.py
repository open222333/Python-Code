

def get_worker_hostname():
    from celery import current_task

    # 取得 worker hostname
    hostname = current_task.request.hostname
    return hostname


def get_worker_info():
    from billiard.process import current_process

    p = current_process()
    return p.name, p.ident, p._parent_pid
