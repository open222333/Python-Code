from configparser import ConfigParser
import os


config = ConfigParser()
config_file = f'{os.path.dirname(__file__)}/config.ini'
config.read(config_file, encoding='utf-8')

test = config.get('headers', 'TEST')
print(test, type(test))
