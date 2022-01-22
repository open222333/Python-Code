from configparser import ConfigParser
import os


config = ConfigParser()
config.read(
    f'{os.path.dirname(__file__)}/test_config.ini',
    encoding='utf-8'
)
DBNAME = config['SQLALCHEMY']['DBNAME']
