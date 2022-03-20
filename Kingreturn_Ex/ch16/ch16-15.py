# 使用?問號做搜尋 (na)? na可有可無
import re
# 測試1
msg = 'Johnson will attend my party tonight.'
pattern = 'John((na)?son)'
txt = re.search(pattern, msg)  # 傳回搜尋結果
print(txt.group())
# 測試2
msg = 'Johnnason will attend my party tonight.'
pattern = 'John((na)?son)'
txt = re.search(pattern, msg)  # 傳回搜尋結果
print(txt.group())
