# 計算時薪
wage = 150  # 時薪
work_hours = eval(input("請輸入工作時數："))
if work_hours > 50:
    print("時薪：", work_hours * wage * 1.6)
elif work_hours > 40:
    print("時薪：", work_hours * wage * 1.2)
elif work_hours == 40:
    print("時薪：", work_hours * wage)
else:
    print("時薪：", work_hours * wage * 0.8)
