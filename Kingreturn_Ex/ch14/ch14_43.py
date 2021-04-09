# 解壓縮zip檔案
import zipfile

fileUnZip = zipfile.ZipFile('ch14/out41.zip')
fileUnZip.extractall('ch14/out43')
fileUnZip.close()
