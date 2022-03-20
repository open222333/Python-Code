# groups() areaNum,localNum = phoneNum.groups() # 多重指定
import re

msg = 'Please call my sercretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)  # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()  # 留意是groups()
print("區域號碼是：%s" % areaNum)  # 顯示區域號碼
print("電話號碼是：%s" % localNum)  # 顯示電話號碼
