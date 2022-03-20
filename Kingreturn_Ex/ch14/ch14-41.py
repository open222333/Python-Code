# 檔案壓縮與解壓縮zipFile
import zipfile
import glob
import os

fileZip = zipfile.ZipFile('ch14/out41.zip', 'w')
for name in glob.glob('ch14/zipdir41/*'):  # 遍歷zipdir41目錄
    fileZip.write(name, os.path.basename(name),
                  zipfile.ZIP_DEFLATED)  # ZIP_DEFLATED註明壓縮方式
fileZip.close()
