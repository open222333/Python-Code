import zipfile

src = input("請輸入要解壓縮的來源檔案名：")
dst = input("請輸入要解壓縮到的目的檔案名：")
zipunFile = zipfile.ZipFile(src)
zipunFile.extractall(dst)
zipunFile.close()
