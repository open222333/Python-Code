# 字元分類的^字元 搜尋不在字元內的字元
import re

# 測試1搜尋不在[aeiouAEIOU]的字元
msg = 'John,Johnson,Johnnason and Johnnathan will attend my party tonight.'
pattern = '[^aeiouAEIOU]'
txt = re.findall(pattern,msg)
print(txt)
# 測試2搜尋不在[2-5.]的字元
msg = '1 cat, 2 dogs, 3 pigs, 4 swans'
pattern = '[^2-5.]'
txt = re.findall(pattern,msg)
print(txt)