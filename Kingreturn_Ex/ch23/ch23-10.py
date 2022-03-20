# 錯誤網址的異常處理
import requests

url = 'http://www.gzaxxc.com/file_not_existed'  # 不存在的內容
try:
    htmlfile = requests.get(url)
    print('下載成功')
except Exception as err:
    print("下載網頁失敗：%s" % err)
