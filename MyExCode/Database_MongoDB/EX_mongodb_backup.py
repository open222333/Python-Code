import os
from configparser import ConfigParser
from datetime import datetime


def mongodump(host, db, col, target_dir='~/Desktop/'):
    '''備份 mongo集合
    target_dir: 目標位置'''
    date = datetime.now().__format__('%Y%m%d%H%M')
    target_path = f'{target_dir}mongo_backup_{col}/{date}'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    command = f'mongodump -h {host} -d {db} -c {col} -o {target_path}'
    print(command)
    os.system(command)


def mongorestore(host, db, col, target_path):
    '''備份 mongo集合'''
    if not os.path.exists(target_path):
        print(f'{target_path} no exists')
    command = f'mongorestore -h {host} -d {db} -c {col} {target_path}/{db}/{col}.bson'
    print(command)
    os.system(command)


os.chdir(os.path.dirname(__file__))
config = ConfigParser()
config.read('mongo_backup_config.ini', encoding='utf-8')

host = config.get('MONGO', 'MONGO_HOST')
db = config.get('MONGO', 'MONGO_DB')
col = config.get('MONGO', 'MONGO_COLLECTION')
target_dir = config.get('MONGO', 'TARGET_PATH')

local_host = config.get('MONGO', 'MONGO_LOCAL_HOST')
date = config.get('MONGO', 'DATE')
target = f'{target_dir}mongo_backup_{col}/{date}'

if bool(int(config.get('MONGO', 'MONGO_DUMP'))):
    mongodump(host=host, db=db, col=col, target_dir=target_dir)

if bool(int(config.get('MONGO', 'MONGO_RESTORE'))):
    mongorestore(host=local_host, db=db, col=col, target_path=target, col_name=f'{col}_{date}')
