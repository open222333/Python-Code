# 搜尋時使用大括號設定比對次數
import re


def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:  # 搜尋失敗
        print("搜尋失敗", txt)
    else:  # 搜尋成功
        print("搜尋成功", txt.group())


msg1 = 'son'
msg2 = 'sonson'
msg3 = 'sonsonson'
msg4 = 'sonsonsonson'
msg5 = 'sonsonsonsonson'
pattern = '(son){2,}'
#pattern = '(son){,5}'
searchStr(pattern, msg1)
searchStr(pattern, msg2)
searchStr(pattern, msg3)
searchStr(pattern, msg4)
searchStr(pattern, msg5)
