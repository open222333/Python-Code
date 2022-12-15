# 選擇輸入的溫度 華氏或攝氏
temperature_type = input("攝氏溫度(請輸入c)，華氏溫度(請輸入f)：")
if temperature_type == 'c':
    c = eval(input("請輸入攝氏溫度："))
    print("{0:3.2f}".format(c * 9 / 5 + 32))
elif temperature_type == 'f':
    f = eval(input("請輸入華氏溫度："))
    print("{0:3.2f}".format((f - 32) * 5 / 9))
else:
    print("輸入錯誤指令")
