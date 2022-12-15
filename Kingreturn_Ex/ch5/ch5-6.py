# 輸入歲數計算票價
print("計算票價")
age = input("請輸入年齡：")
age = int(age)
ticket = 100  # 票價100
if age >= 80 or age <= 6:  # 年齡大於等於80歲或小於等於6歲 打2折
    ticket = ticket * 0.2
    print("票價是：%d" % ticket)
elif age >= 60 or age <= 12:  # 年齡60-79歲或7-12歲 打5折
    ticket = ticket * 0.5
    print("票價是：%d" % ticket)
else:
    print("票價是：%d" % ticket)
