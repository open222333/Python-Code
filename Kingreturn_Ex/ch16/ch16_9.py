# 使用小掛號分組 re.findall() 傳回元組的串列 元組類的元素是分組的內容
import re

msg = 'Please call my sercretary using 02-26669999 or 02-11112222'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.findall(pattern, msg)  # 傳回搜尋結果

print(phoneNum)