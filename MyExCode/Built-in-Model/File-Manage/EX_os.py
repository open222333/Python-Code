import os
import shutil


def get_environ():
    # 顯示 環境變數
    return os.environ


def get_filename(path):
    # 顯示檔案名
    return os.path.basename(path)


def get_file_extension(file_path):
    '''取得 副檔名'''
    _, extension = os.path.splitext(file_path) # 路徑 以及副檔名
    return extension


def create_dir(path):
    if not os.path.exists(path):
        # 創建多層次資料夾
        os.makedirs(path)


def remove_dir(path):
    if os.path.exists(path):
        # 刪除資料夾
        shutil.rmtree(path)


def show_all_files(path):
    '''顯示資料夾所有檔案 包含子資料夾'''
    if not os.path.isdir(path):
        return f'{path} not a directory'
    files = os.listdir(path)
    for file in files:
        if '.' not in file:
            files.remove(file)
            files.extend(os.listdir(f'{path}/{file}'))
    files.sort()
    return files
