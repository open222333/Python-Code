import shutil

src = input("請輸入複製的來源檔案名：")
dst = input("請輸入複製的目的檔案名：")
shutil.copy(src, dst)
