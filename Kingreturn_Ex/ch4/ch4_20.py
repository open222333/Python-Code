# 專題 溫度轉換 輸入華氏溫度 輸出攝氏溫度
f = input("請輸入華氏溫度：")
c = (int(f) - 32) * 5 / 9
print("華氏 %s 等於攝氏 %4.1f" % (f, c))
