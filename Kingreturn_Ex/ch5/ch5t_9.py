# 擴充 ch5_9.py
height = input("請輸入身高（公分）：")
weight = input("請輸入體重（公斤）：")
bmi = int(weight) / ((float(height) / 100) ** 2)
if bmi < 18.5:
    print("體重過低")
elif 23.9 > bmi >= 18.5:
    print("體重正常")
elif 24 > bmi > 27.9:
    print("超重")
else:
    print("肥胖")
