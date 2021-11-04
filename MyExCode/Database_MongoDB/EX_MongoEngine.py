'''
MongoEngine 文檔
https://docs.mongoengine.org/guide/querying.html
'''
from mongoengine import connect

# 連接
connect('project1')
connect(host="mongodb://127.0.0.1:27017/my_db")
# Connects to 'my_db' database by authenticating
# with given credentials against the 'admin' database (by default as authSource isn't provided)
connect(host="mongodb://my_user:my_password@127.0.0.1:27017/my_db")

# Equivalent to previous connection but explicitly states that
# it should use admin as the authentication source database
connect(host="mongodb://my_user:my_password@hostname:port/my_db?authSource=admin")

# Connects to 'my_db' database by authenticating
# with given credentials against that same database
connect(host="mongodb://my_user:my_password@127.0.0.1:27017/my_db?authSource=my_db")

connect(
    db='test',
    username='user',
    password='12345',
    host='mongodb://admin:qwerty@localhost/production'
)
