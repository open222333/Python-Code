# 今天星期日 輸入天數 輸出星期幾
week_days = eval(input("輸入幾天後："))
if week_days % 7 == 0:
    print("日")
elif week_days % 7 == 1:
    print("一")
elif week_days % 7 == 2:
    print("二")
elif week_days % 7 == 3:
    print("三")
elif week_days % 7 == 4:
    print("四")
elif week_days % 7 == 5:
    print("五")
else:
    print("六")
