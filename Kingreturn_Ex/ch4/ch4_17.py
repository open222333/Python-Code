# 處理字串的數學運算eval()
numberStr = input("請輸入數值公式：")
number = eval(numberStr)
print("計算結果：%5.2f" % number)
