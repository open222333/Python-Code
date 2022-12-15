from configparser import ConfigParser
import os

config = ConfigParser()
config.read(f'{os.path.dirname(__file__)}/test_config.ini', encoding='utf-8')

SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY']['SQLALCHEMY_DATABASE_URI']
SPEED_TEST_SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY']['SPEED_TEST_SQLALCHEMY_DATABASE_URI']
USER_WATCH_SQLALCHEMY_DATABASE_URI = config['SQLALCHEMY']['USER_WATCH_SQLALCHEMY_DATABASE_URI']
