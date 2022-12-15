# 奇數偶數的判斷
print("奇數偶數的判斷")
num = input("請輸入任意整數：")
rem = int(num) % 2
if rem == 0:
    print("%d 是偶數" % int(num))
else:
    print("%d 是奇數" % int(num))
