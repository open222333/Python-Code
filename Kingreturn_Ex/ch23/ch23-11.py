# 儲存下載的網頁
import requests

url = 'https://deepmind.com.tw'  # 網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:
    print("網頁下載失敗： %s" % err)

# 儲存網頁內容
fn = 'ch23/out23_11.txt'
with open(fn, 'wb') as file_Obj:  # 以二進位儲存
    for diskStorage in htmlfile.iter_content(10240):  # Response物件處理
        size = file_Obj.write(diskStorage)  # Response物件寫入
        print(size)  # 列出每次寫入大小
    print("以%s 儲存網頁HTML檔案成功" % fn)  # 列出每次寫入大小
