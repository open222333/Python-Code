# 輸入資料input() 認識輸入資料型態
print("歡迎使用成績輸入系統")
name = input("請輸入姓名：")
engh = input("請輸入英文成績：")
math = input("請輸入數學成績：")
total = int(engh) + int(math)
print("%s你的總分是%d" % (name, total))
