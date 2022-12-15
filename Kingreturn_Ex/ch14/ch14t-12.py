import zipfile
import glob
import os

src = input("請輸入需壓縮的來源檔案名：")
dst = input("請輸入要壓縮到的目的檔案名：")

fileZip = zipfile.ZipFile((dst + '.zip'), 'w')
for name in glob.glob((src + '/*')):
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)

fileZip.close()
