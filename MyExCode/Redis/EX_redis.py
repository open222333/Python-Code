import redis
'''https://redis-py.readthedocs.io/en/stable/#'''
# redis_host = 'localhost'
redis_host = '127.0.0.1'
redis_port = 31119

# 連接池 可以直接建立連接池 可實現多個Redis實例共享一個池
# 使用 ConnectionPool
pool = redis.ConnectionPool(
    host=redis_host,
    port=redis_port,
    decode_responses=True
)
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
# decode_responses: redis 取出默認是 bytes，此參數轉為字串

r.set('name', 'runoob')  # 設置name對應值
# set(name, value, ex=None, px=None, nx=False, xx=False)
print(r['name'])
print(r.get('name'))  # 取出鍵 name對應的值
print(type(r.get('name')))
