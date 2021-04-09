# 使用小掛號分組
import re

msg = 'Please call my sercretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)  # 傳回搜尋結果

print("完整號碼是：%s" % phoneNum.group())  # 顯示完整號碼
print("完整號碼是：%s" % phoneNum.group(0))  # 顯示完整號碼
print("區域號碼是：%s" % phoneNum.group(1))  # 顯示區域號碼
print("電話號碼是：%s" % phoneNum.group(2))  # 顯示電話號碼
