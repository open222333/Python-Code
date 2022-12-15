from configparser import ConfigParser
import os
'''https://docs.python.org/zh-tw/3/library/configparser.html#supported-ini-file-structure'''

config = ConfigParser()

config_file = f'{os.path.dirname(__file__)}/config.ini'
config.read(config_file, encoding='utf-8')
# config.set('dev', 'test')
# test = config.get('Frameworks', 'PATH')
# print(test, type(test))
print(config['TEST']['PATH'])


# print(config.sections())
