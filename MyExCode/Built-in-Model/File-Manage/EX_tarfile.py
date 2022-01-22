'''
解壓縮 zip檔案 tar檔案
'''

import tarfile


def decompressTarFile(source_dir, source_file, destination_dir):
    tar_file = tarfile.open(f'{source_dir}/{source_file}', 'r')
    file_list = tar_file.getnames()

    for i in range(0, len(file_list)):
        file_in_tar = tar_file.getmember(file_list[i])
        try:
            tar_file.extract(file_in_tar, destination_dir)
        except:
            continue
    return
