import pyzipper


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
