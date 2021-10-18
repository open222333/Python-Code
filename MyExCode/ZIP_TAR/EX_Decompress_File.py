'''
解壓縮 zip檔案 tar檔案
'''
import pyzipper
import tarfile


def decompressZipFile(source_dir, source_file, destination_dir, decompress_password=None):
    '''解壓縮 zip檔案'''
    with pyzipper.AESZipFile(f'{source_dir}/{source_file}') as zip_file:
        if decompress_password is not None:
            zip_file.setpassword(decompress_password)

        zip_file.extract(zip_file.getinfo(file_list[i]), destination_dir)

        # file_list = zip_file.namelist()
        # for i in range(0, len(file_list)):
        #     try:
        #         zip_file.extract(zip_file.getinfo(
        #             file_list[i]), destination_dir)
        #     except:
        #         continue


def decompressTarFile():
    pass
