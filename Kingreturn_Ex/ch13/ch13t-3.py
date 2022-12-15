# random模組 猜數字遊戲
import random  # 導入模組random

min, max = 1, 30
ans = random.randint(min, max)  # 隨機數產生答案
count = 0  # 紀錄猜的次數
while True:
    yourNum = int(input("請猜1-30之間數字(若輸入Q或q則結束程式)："))
    if yourNum == ans:
        print("恭喜！答對了")
        count += 1
        print("共猜了%d次" % count)
        break
    elif yourNum == 'Q' or yourNum == 'q':
        break
    elif yourNum < ans:
        print("請猜大一點")
        count += 1
    else:
        print("請猜小一點")
        count += 1
