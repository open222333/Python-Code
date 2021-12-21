import os
from datetime import datetime


def mongodump(host, db, col):
    '''備份 mongo集合'''
    date = datetime.now().__format__('%Y%m%d')
    target_path = f'/Users/4ge0/Desktop/mongo_backup_avdata_videos/{date}'
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    command = f'mongodump -h {host} -d {db} -c {col} -o {target_path}'
    os.system(command)
