# 讀取zip檔案
import zipfile

listZipinfo = zipfile.ZipFile('ch14/out41.zip', 'r')
print(listZipinfo.namelist())  # 以列表列出所有壓縮檔案
print('\n')
for info in listZipinfo.infolist():
    print(info.filename, info.file_size, info.compress_size)  # 檔案名 檔案大小 壓縮結果大小
