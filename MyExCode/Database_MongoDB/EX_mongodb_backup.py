import os
from datetime import datetime


def mongodump(host, db, col, target_dir='~/Desktop/'):
    '''備份 mongo集合
    target_dir: 目標位置'''
    date = datetime.now().__format__('%Y%m%d%H%M')
    target_path = f'{target_dir}mongo_backup_{col}/{date}'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    command = f'mongodump -h {host} -d {db} -c {col} -o {target_path}'
    os.system(command)


def mongorestore(host, db, col, target_path):
    '''備份 mongo集合'''
    if not os.path.exists(target_path):
        return False
    command = f'mongorestore -h {host} -d {db} -c {col} {target_path}/{db}/{col}.bson'
    os.system(command)
    return True
