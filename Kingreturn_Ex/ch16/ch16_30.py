# 單一字元使用萬用字元"."
import re

msg = 'cat hat sat at matter flat'
pattern = '.at'
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
