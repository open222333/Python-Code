# 將整數轉成字元 將字元以及中文字轉成unicode碼值
x1 = 97
x2 = chr(x1)
print(x2)  # 輸出數值97的字元
x3 = ord(x2)
print(x3)  # 輸出unicode值(10進位)
x4 = "魁"
print(hex(ord(x4)))  # 輸出unicode值(16進位)
