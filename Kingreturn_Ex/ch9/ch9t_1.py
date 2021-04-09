week = {'Monday': '星期一', 'Tuesday': '星期二', 'Wednesday': '星期三',
        'Thursday': '星期四', 'Friday': '星期五', 'Saturday': '星期六', 'Sunday': '星期日'}
inputwd = input("請輸入星期英文：")
if inputwd.title() not in week:
    print("輸入錯誤")
else:
    print(week[inputwd.title()])
