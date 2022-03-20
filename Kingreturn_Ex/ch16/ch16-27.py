# 正則表示法的^字元
import re
# 測試1 搜尋John字串在最前面
msg = 'John will attend my party tonight.'
pattern = '^John'
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試2 搜尋John字串不是在最前面
msg = 'My best friend is John'
pattern = '^John'
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
