import os
import shutil


def get_environ():
    # 顯示 環境變數
    return os.environ


def get_home():
    '''回傳home資料夾'''
    return os.path.expanduser('~')


def get_home_2():
    '''回傳home資料夾'''
    from pathlib import Path
    return str(Path.home())


def get_filename(path):
    # 顯示檔案名
    return os.path.basename(path)


def get_file_extension(file_path):
    '''取得 副檔名'''
    _, extension = os.path.splitext(file_path)  # 路徑 以及副檔名
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


def get_all_files(dir_path, extensions=None):
    '''取得所有檔案
    dir_path: 檔案資料夾
    extensions: 指定副檔名,若無指定則全部列出
    '''
    target_file_path = []
    path = os.path.abspath(dir_path)

    for file in os.listdir(path):
        _, file_extension = os.path.splitext(file)
        if extensions:
            allow_extension = [f'.{e}' for e in extensions]
            if file_extension in allow_extension:
                target_file_path.append(f'{path}/{file}')
        else:
            target_file_path.append(f'{path}/{file}')

        # 遞迴
        if os.path.isdir(f'{dir_path}/{file}'):
            files = get_all_files(f'{dir_path}/{file}', extensions)
            for file in files:
                target_file_path.append(file)
    target_file_path.sort()
    return target_file_path
