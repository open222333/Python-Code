# 處理字串的數學運算eval() 重新設計ch4_15.py
print("歡迎使用成績輸入系統")
name = input("請輸入姓名：")
engh = eval(input("請輸入英文成績："))
math = eval(input("請輸入數學成績："))
total = engh + math
print("%s你的總分是%d" % (name, total))
