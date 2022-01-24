from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import time
from config import SQLALCHEMY_DATABASE_URI, USER_WATCH_SQLALCHEMY_DATABASE_URI, SPEED_TEST_SQLALCHEMY_DATABASE_URI


'''flask-sqlachemy 練習'''

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_BINDS = {
    'speed_test_log': SPEED_TEST_SQLALCHEMY_DATABASE_URI,
    'user_watch_log': USER_WATCH_SQLALCHEMY_DATABASE_URI
}
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_recycle': 250,
    'max_overflow': 5,
    'pool_size': 100,
    'pool_pre_ping': True,
    'pool_use_lifo': True,
}
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = SQLALCHEMY_ENGINE_OPTIONS

sqlalchemy = SQLAlchemy(app)


class Test(sqlalchemy.Model):
    id = Column(Integer, primary_key=True)
    test_data = Column(String(100))


data = Test.query.all()
time.sleep(100)
print(data)