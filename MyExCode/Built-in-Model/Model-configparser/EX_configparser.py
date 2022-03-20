from configparser import ConfigParser
from os.path import dirname


def get_value(key):
    conf = ConfigParser()
    conf.read(f'{dirname(__file__)}/config.ini', encoding='utf-8')
    if key in conf['TEST']:
        return conf['TEST'][key]


config = get_value()