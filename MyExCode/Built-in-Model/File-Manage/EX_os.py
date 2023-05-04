import os
import shutil
from typing import Union


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


def get_all_files(dir_path, extensions=None, add_abspath=False):
    '''取得所有檔案

    dir_path: 檔案資料夾
    extensions: 指定副檔名,若無指定則全部列出
    add_abspath: 列出 絕對路徑
    '''
    target_file_path = []
    path = os.path.abspath(dir_path)

    for file in os.listdir(path):

        if add_abspath:
            target_path = f'{path}/{file}'
        else:
            target_path = f'{file}'

        _, file_extension = os.path.splitext(file)
        if extensions:
            allow_extension = [f'.{e}' for e in extensions]
            if file_extension in allow_extension:
                target_file_path.append(target_path)
        else:
            target_file_path.append(target_path)

        # 遞迴
        if os.path.isdir(f'{dir_path}/{file}'):
            files = get_all_files(f'{dir_path}/{file}', extensions)
            for file in files:
                target_file_path.append(file)
    target_file_path.sort()
    return target_file_path


def split_file(path: str, chunk_size: int = 500000000, filename: str = None):
    """分割檔案

    Args:
        path (str): 檔案路徑
        chunk_size (int): 分割大小 byte
        filename (str, optional): 檔名. Defaults to None.
    """
    file_number = 1

    if not filename:
        filename = os.path.basename(path)
    file_dir = os.path.dirname(path)
    _, file_extension = os.path.splitext(path)

    with open(path, 'rb') as f:
        chunk = f.read(chunk_size)
        while chunk:
            with open(f'{file_dir}/{filename}._{str(file_number)}{file_extension}', 'wb') as chunk_file:
                chunk_file.write(chunk)
            file_number += 1
            chunk = f.read(chunk_size)


def cat_files():
    pass


# https://stackoverflow.com/questions/546508/how-can-i-split-a-file-in-python
def split_file_sample(file, prefix, max_size, buffer=1024):
    """
    file: the input file
    prefix: prefix of the output files that will be created
    max_size: maximum size of each created file in bytes
    buffer: buffer size in bytes

    Returns the number of parts created.
    """
    with open(file, 'r+b') as src:
        suffix = 0
        while True:
            with open(prefix + '.%s' % suffix, 'w+b') as tgt:
                written = 0
                while written < max_size:
                    data = src.read(buffer)
                    if data:
                        tgt.write(data)
                        written += buffer
                    else:
                        return suffix
                suffix += 1


def cat_files_sample(infiles, outfile, buffer=1024):
    """
    infiles: a list of files
    outfile: the file that will be created
    buffer: buffer size in bytes
    """
    with open(outfile, 'w+b') as tgt:
        for infile in sorted(infiles):
            with open(infile, 'r+b') as src:
                while True:
                    data = src.read(buffer)
                    if data:
                        tgt.write(data)
                    else:
                        break


def split_file(path: str, chunk_size: int = 500000000, filename: str = None):
    """使用split 分割檔案

    Args:
        path (str): 檔案路徑
        chunk_size (int): 分割大小 byte. Defaults to 500000000.
        filename (str, optional): 檔名. Defaults to None.
    """
    if not filename:
        filename = os.path.basename(path)
    file_dir = os.path.dirname(path)

    command = f'split -b {chunk_size} {path} {file_dir}/{filename}_'

    print(command)
    os.system(command)


def get_all_files(path: str, extensions: Union[int, float, None] = None, add_abspath: bool = False, exclude_dir: bool = True) -> list[str]:
    """取得所有檔案

    Args:
        path (str): 檔案資料夾
        extensions (Union[int, float, None], optional): 指定副檔名,若無指定則全部列出. Defaults to None.
        add_abspath (bool, optional): 列出 絕對路徑. Defaults to False.
        exclude_dir (bool, optional): 排除資料夾. Defaults to True.

    Returns:
        list[str]: 回傳串列
    """
    target_file_path = []
    path = os.path.abspath(path)

    for file in os.listdir(path):

        is_dir = False

        if exclude_dir:
            is_dir = os.path.isdir(file)

        if not is_dir:
            if add_abspath:
                target_path = f'{path}/{file}'
            else:
                target_path = f'{file}'

            _, file_extension = os.path.splitext(file)
            if extensions:
                allow_extension = [f'.{e}' for e in extensions]
                if file_extension in allow_extension:
                    target_file_path.append(target_path)
            else:
                target_file_path.append(target_path)

        # 遞迴
        if os.path.isdir(f'{path}/{file}'):
            files = get_all_files(f'{path}/{file}', extensions)
            for file in files:
                target_file_path.append(file)

    target_file_path.sort()
    return target_file_path


def human_readable_size(size: int, decimal_places: int = 2) -> str:
    """人類可讀 檔案大小

    https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
    Args:
        size (int): 檔案大小 (bytes)
        decimal_places (int, optional): 顯示小數位. Defaults to 2.

    Returns:
        str: 檔案大小 單位
    """
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
        if size < 1024.0 or unit == 'PiB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"
