# 將搜尋字串的部分內容取代
import re
# 使用隱藏文字執行取代
msg = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
pattern = r'CIA (\w)\w*'  # 欲搜尋FBI + 空一格後的名字
newstr = r'\1***'  # 新字串使用隱藏文字
txt = re.sub(pattern, newstr, msg)  # 執行取代
print("取代成功：", txt)
