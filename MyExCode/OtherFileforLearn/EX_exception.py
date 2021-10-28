import sys
import traceback

'''
[Python] 當Exception發生時，怎麼抓它發生的位置以及詳細原因？
https://dotblogs.com.tw/caubekimo/2018/09/17/145733
'''

try:
    list_t = []
    print(list_t[0])
except Exception as e:
    error_class = e.__class__.__name__  # 取得錯誤類型
    detail = e.args[0]  # 取得詳細內容
    cl, exc, tb = sys.exc_info()  # 取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
    fileName = lastCallStack[0]  # 取得發生的檔案名稱
    lineNum = lastCallStack[1]  # 取得發生的行號
    funcName = lastCallStack[2]  # 取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(
        fileName, lineNum, funcName, error_class, detail)
    print(errMsg)


    print(traceback.format_exc())
