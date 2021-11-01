'''
解壓縮 zip檔案 tar檔案
'''
import pyzipper
import tarfile


def decompressZipFile(source_dir, source_file, destination_dir, decompress_password=None):
    '''
    解壓縮 zip檔案
    無法辨認 ~/ 為使用者資料夾
    '''
    with pyzipper.AESZipFile(f'{source_dir}/{source_file}') as zip_file:
        # 若有AES加密的密碼
        if decompress_password is not None:
            zip_file.setpassword(decompress_password)

        # 壓縮檔內的檔案列表
        file_list = zip_file.namelist()
        for i in range(0, len(file_list)):
            try:
                file_in_zip = zip_file.getinfo(file_list[i])
                zip_file.extract(file_in_zip, destination_dir)
            except:
                continue
    return


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


# pyzipper 作者 提供的範例
secret_password = b'lost art of keeping a secret'

with pyzipper.AESZipFile('new_test.zip',
                         'w',
                         compression=pyzipper.ZIP_LZMA) as zf:
    zf.setpassword(secret_password)
    zf.setencryption(pyzipper.WZ_AES, nbits=128)
    zf.writestr('test.txt', "What ever you do, don't tell anyone!")

with pyzipper.AESZipFile('new_test.zip') as zf:
    zf.setpassword(secret_password)
    my_secrets = zf.read('test.txt')
