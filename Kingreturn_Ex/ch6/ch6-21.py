# rstrip() lstrip() strip() 刪除空白字元應用
strN = ' DeepStone '
strL = strN.lstrip()  # 刪除左邊多餘空白
strR = strN.rstrip()  # 刪除右邊多餘空白
strB = strN.lstrip()  # 先刪除左邊多餘空白
strB = strB.rstrip()  # 再刪除右邊多餘空白
strO = strN.strip()  # 一次刪除頭尾多餘空白
print("/%s/" % strN)
print("/%s/" % strL)
print("/%s/" % strR)
print("/%s/" % strB)
print("/%s/" % strO)
