# in 和not in 運算式的應用
password = 'deepstone'
ch = input("請輸入字元 ＝ ")
print("in運算式")
if ch in password:
    print("輸入字元在密碼中")
else:
    print("輸入字元不在密碼中")

print("not in 運算式")
if ch not in password:
    print("輸入字元不在密碼中")
else:
    print("輸入字元在密碼中")
