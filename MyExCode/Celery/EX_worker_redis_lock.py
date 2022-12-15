import redis

have_lock = False
my_lock = redis.Redis().lock("my_key")
try:
    have_lock = my_lock.acquire(blocking=True)
    if have_lock:
        print("Got lock.")
    else:
        print("Did not acquire lock.")

finally:
    if have_lock:
        my_lock.release()
