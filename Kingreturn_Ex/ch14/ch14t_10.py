from os import WIFCONTINUED


src = input("請輸入複製的來源檔案名：")
dst = input("請輸入複製的目的檔案名：")

with open(src, 'rb') as rfile:
    tmp = rfile.read()
    with open(dst, 'wb') as wfile:
        wfile.write(tmp)
