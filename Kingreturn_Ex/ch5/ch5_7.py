# 輸入字元 輸出此字元是大寫小寫阿拉伯數字或特殊字元
print("判斷輸入字元類別")
ch = input("請輸入字元：")
if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
    print("這是大寫字母")
elif ord(ch) >= ord("a") and ord(ch) <= ord("z"):
    print("這是小寫字母")
elif ord(ch) >= ord("0") and ord(ch) <= ord("9"):
    print("這是數字")
else:
    print("這是特殊字元")
