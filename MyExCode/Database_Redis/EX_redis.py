import redis
'''官方文檔
https://redis-py.readthedocs.io/en/stable/#'''
# redis_host = 'localhost'
redis_host = '127.0.0.1'
# redis_host = 'redis_test'
redis_port = 6379


# r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
# # decode_responses: redis 取出默認是 bytes，此參數轉為字串


# 連接池 可以直接建立連接池 可實現多個Redis實例共享一個池
# 使用 ConnectionPool
pool = redis.ConnectionPool(
    host=redis_host,
    port=redis_port,
    db=10,
    decode_responses=True
)
r = redis.Redis(connection_pool=pool)

# set(name, value, ex=None, px=None, nx=False, xx=False)
print(r.set('name1', 'runoob'))  # 設置name對應值
print(r.setnx('name', 'runoob1'))  # setnx name不存在才添加 回傳 False

# 列出所有key
print(r.keys())
print(r['name'])
print(r.get('name'))  # 取出鍵 name對應的值
# print(type(r.get('name')))

# 根據key刪除資料
r.delete('name1')
